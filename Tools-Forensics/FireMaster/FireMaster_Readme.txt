
FireMaster 
https://SecurityXploded.com/firemaster.php
*****************************************************************************
		            						
											
											
************  Check New GUI Version **************

FireMasterCracker  
https://securityxploded.com/firefox-master-password-cracker.php

********************************************
            						
	            						

			
FireMaster is the FREE tool to recover your forgotten master password of all Mozilla based apps like Firefox, Thunderbird, InstantBird, SeaMonkey etc  


Here is the usage information
------------------------------

 Firemaster [-q]
            [ [-d -f <dict_file>]
            [-h -f <dict_file> [-n <length>] [-g "charlist"] [ -s | -p ] ]
            [-b -m <length> -l <length> [-c "charlist"] -p "pattern"]
            "<Firefox_Profile_Path>"


 Note: You can specify 'auto' (without quotes) in place of "<Firefox_Profile_Path>" to automatically detect default profile path.

 -q        Quiet mode. Disable verbose messages & prompts during recovery operation


 Dictionary Crack Options:
 -d        Perform dictionary crack operation
 -f        Dictionary file with words on each line


 Hybrid Crack Options:
 -h        Perform hybrid crack operation using dictionary passwords
           Hybrid crack can find passwords like pass123, 123pass etc
 -f        Dictionary file with words on each line
 -g        Group of characters used for generating the strings
 -n        Maximum length of strings to be generated using above character list
           These strings are added to the dictionary word to form the password
 -s        Suffix the generated chars to the dictionary word(pass123)
 -p        Prefix the generated chars to the dictionary word(123pass)


 Bruteforce Crack Options:
 -b        Perform bruteforce crack
 -c        Character list used for bruteforce cracking process
 -m        [Optional] Specify the minimum length of password
 -l        Specify the maximum length of password
 -p        [Optional] Specify the pattern for the password



 Examples of usage
---------------------

 // Dictionary Crack
 FireMaster.exe -d -f c:\dictfile.txt auto

 // Hybrid Crack
 FireMaster.exe -h -f c:\dictfile.txt -n 3 -g "123" -s auto

 // Bruteforce Crack
 FireMaster.exe -q -b -m 3 -l 10 -c "abcdetps123" "c:\my test\firefox"

 // Bruteforce Crack with pattern - [recommended]
 FireMaster.exe -q -b -m 3 -l 10 -c "abcdetps123" -p "pa??f??123" auto
 
 
Here Firefox_Profile_Path refers to the Firefox profile directory where key3.db file is present.

This points to the Firefox profile directory 
(Eg: C:\Documents and Settings\<user>\Application Data\Mozilla\Firefox\Profiles\<prof name>) 
on your machine. However you can also copy key3.db file from any other machine 
such as Linux/MAC PC to your local windows machine and specify that path during 
recovering operation.

With version 5.0 onwards you can specify 'auto' (without quotes) in place of "<Firefox_Profile_Path>" to automatically detect default profile path.

Quiet mode ( -q option ) will disable printing each password while recovery is in progress.
This makes it much faster especially for brute force operation. However during brute force 
operation if the password count exceeds 50000 passwords then it automatically enters the 
quiet mode.


Hybrid method tries normal dictionary password as well as password created by appending/prefixing
the generated strings to the dictionary word. For example if the dictionary word is "test" and you
have specified character set as '123' (-c 123 -s) then the new passwords will be test1, test12, 
test123, test32 etc. Character list (-g for hybrid and -c for brute force) specifies the characters 
to be used for generating passwords. If you don't specify then the default character list is used. 

For brute force -m indicates the minimum length of password to be generated. This can reduce the 
generated passwords and hence the time considerably when large number of character set is specified. 
Similarly -l (small 'L') specifies the maximum length of password to be generated. For example, if you 
specify -m 6 and -l 8 then only passwords which are of length at least 6 and above but below 8 will 
be generated. 


Now you can reduce the password cracking time significantly using pattern based password recovery
mechanism. If you know that password is of certain length and also remember few characters then you 
can specify that pattern for brute force cracking. For example, assume that you have set the master 
password of length 12 and it begins with 'fire' and ends with '123' then command will look like below 

FireMaster.exe -b -c "abyz" -l 12 -p "fire?????123" c:\testpath 

This will reduce the time to seconds which otherwise would have taken days or hours to crack that
password. You can even crack the impossible looking passwords using the right pattern.

For more details on pattern based password recovery mechanism, refer to blog post
http://nagareshwar.securityxploded.com/2008/03/31/firemaster-with-pattern-based-password-recovery/


By default FireMaster includes smaller password list file "passlist.txt". You can find larger password dictionary file here
ftp://ftp.openwall.com/pub/wordlists/all.gz


If you have any problems with using FireMaster then write to contact@securityxploded.com

Good Luck..!

The SX Team, 
https://securityxploded.com/firemaster.php



-----------------------------------------------------------------------------------
Finding it difficult?  Try our new Graphics version - FireMasterCracker
https://securityxploded.com/firefox-master-password-cracker.php
-----------------------------------------------------------------------------------
