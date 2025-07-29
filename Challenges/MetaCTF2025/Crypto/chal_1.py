#!/usr/local/bin/python
import time
FLAG = open("flag.txt", "r").read()

def to_seeded_value(s1, s2):
    s = s1 * s2
    for i in range(1,31337*3):
        s+=7
        s*=s1
        s+=s2
        s*=s2
        s+=s1
        s %= 2**16
    return s

def secure_compare(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if to_seeded_value(i, a[i]) ^ to_seeded_value(i, b[i]) != 0:
            return False
    return True

def main():
    print("You can make all the guesses you want, but you don't get to see any inner workings. Can you figure out the flag from the sidelines?")
    
    while True:
        guess = input("Enter your guess: ").strip()
        
        start_time = time.process_time()
        result = secure_compare(guess.encode(), FLAG.encode())
        end_time = time.process_time()
        
        print(f"Time taken: {(end_time - start_time) * 1000000:.2f} microseconds")
        
        if result:
            print("Congratulations! You found the flag!")
            break
        else:
            print("Incorrect guess, try again!")

if __name__ == "__main__":
    main()

