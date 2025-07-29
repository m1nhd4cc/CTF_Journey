
{-# LANGUAGE LambdaCase #-}
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use <$>" #-}
import Data.List
import Data.Word (Word8, Word32)
import Control.Applicative
import Data.Char
import Numeric (readHex)
import Debug.Trace

-- for more information about how to debug consult: https://downloads.haskell.org/ghc/latest/docs/users_guide/debug-info.html
-- some resources:
-- https://gitlab.haskell.org/ghc/ghc/-/wikis/commentary/compiler/generated-code\
-- https://sctf.ehsandev.com/reversing/lambda1.html
-- https://mainisusuallyafunction.blogspot.com/2011/10/thunks-and-lazy-blackholes-introduction.html
-- https://stackoverflow.com/questions/59309340/understanding-how-ghc-compiled-code-works-at-the-lowest-level
-- https://discourse.haskell.org/t/ghc-core-stg-and-cmm-views-on-compiler-explorer/4494

newtype Parser a = P (String -> [(a, String)])

parse :: Parser a -> String -> [(a, String)]
parse (P p) = p

item :: Parser Char
item = P (\case
            [] -> []
            x:xs -> [(x, xs)])

instance Functor Parser where
    fmap :: (a -> b) -> Parser a -> Parser b
    fmap g p  = P (\inp -> case parse p inp of
                        [] -> []
                        [(x, xs)] -> [(g x, xs)])

instance Applicative Parser where
  pure :: a -> Parser a
  pure v = P $ \inp -> [(v, inp)]

  (<*>) :: Parser (a -> b) -> Parser a -> Parser b
  (<*>) pg px = P (\inp -> case parse pg inp of
                        [] -> []
                        [(x, xs)] -> parse (fmap x px) xs)

instance Monad Parser where
  (>>=) :: Parser a -> (a -> Parser b) -> Parser b
  (>>=) p f = P (\inp -> case parse p inp of
                    [] -> []
                    [(x, xs)] -> parse (f x) xs)

instance Alternative Parser where
  empty :: Parser a
  empty = P (const [])

  (<|>) :: Parser a -> Parser a -> Parser a
  (<|>) a b = P (\inp -> case parse a inp of
                    [(x, xs)] -> [(x, xs)]
                    [] -> parse b inp)

sat :: (Char -> Bool) -> Parser Char
sat t = item >>= (\x -> if t x then return x else empty)

charP :: Char -> Parser Char
charP x = sat (== x)

stringP :: [Char] -> Parser [Char]
stringP [] = return []
stringP (x:xs) = do charP x
                    stringP xs
                    return (x:xs)

digitP :: Parser Char
digitP = sat isDigit

natP :: Parser Integer
natP = do   xs <- some digitP
            return (read xs)

hexDigitP :: Parser Char
hexDigitP = sat isHexDigit 

hexToInteger :: (Integral a, Num b) => [a] -> Int -> b
hexToInteger i n = foldr ((\d num -> num * 256 + d) . fromIntegral) 0 (take n i)

hexChar :: Char -> Maybe Int
hexChar ch = elemIndex ch "0123456789ABCDEF"

hexP :: Parser Integer
hexP = do   xs <- some hexDigitP
            case readHex xs of
                [(x, _)] -> return x
                _ -> empty

data DataFlag = DataFlag {
  firstPart :: String,
  secondPart :: Integer,
  thirdPart :: Integer
}

parseFirstFlag :: Parser String
parseFirstFlag = do stringP "CIS2024{"

parseSep :: Parser Char
parseSep = do charP '_'

parseEndFlag :: Parser Char
parseEndFlag = do charP '}'

parseSecondFlag :: Parser String
parseSecondFlag = -- Censor

parseThirdFlag :: Parser Integer
parseThirdFlag = -- Censor

parseFourthFlag :: Parser Integer
parseFourthFlag = -- Censor


flagParser :: Parser DataFlag
flagParser = do 
    parseFirstFlag
    x <- parseSecondFlag
    parseSep
    y <- parseThirdFlag
    parseSep
    z <- parseFourthFlag
    parseEndFlag
    return $ DataFlag x y z

parseFlag :: String -> Bool
parseFlag s = case parse flagParser s of
  [(a, [])] -> True
  _         -> False

main = do
    putStrLn "Please inpput the flag for flag checker"
    a <- getLine
    if parseFlag a then
        putStrLn "All test true"
    else
        putStrLn "Fail"