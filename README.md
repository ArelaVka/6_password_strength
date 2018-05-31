# Password Strength Calculator

The script allows you to analyze the entered password according to the security criteria:
* Length test (check minimal length of password)
* Blacklist test (checks for a word in the blacklist)
* Case sensitivity test (check use of both upper-case and lower-case letters)
* Include number test (check use of numbers)
* Include special symbols test (check use of some special symbols, ex. @, $, etc...)
* Include date or phone test (check that password don't use any date or phone number)

Result of checking is security coefficient (min - 1, max - 10)

Start on Windows (cmd)
```cmd
C:\Python\python.exe C:\password_strength.py <path_to_txt_blacklist>
```

Start on linux (bash)
```bash
$ python password_strength.py <path_to_txt_blacklist>
```

Example:
```cmd
C:\Python\python.exe C:\6_password_strength\password_strength.py C:\6_password_strength\blacklist.txt
Please, enter your password: QWE123!qqwwee

Your password strenght is  10 (max - 10)
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
