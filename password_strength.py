import re
import sys
import os
import argparse


def get_passwords_blacklist(path_to_file):
    with open(path_to_file, 'r') as opened_file:
        return opened_file.read().split()


def get_password_strength(test_password, black_list_path):
    security_point = 1
    min_length_of_password = 6
    if len(test_password) > min_length_of_password:
        print('1) Lenght test - OK')
        security_point += 1
        blacklist = get_passwords_blacklist(black_list_path)
        if test_password in blacklist:
            print('2) Your pass in blacklist - FAILED')
        else:
            print('2) Blacklist test - OK')
            security_point += 1

        if test_password.islower() or test_password.isupper():
            print('3) Case sensitivity test - FAILED')
        else:
            print('3) Case sensitivity test - OK')
            security_point += 2

        if re.findall('\d+', test_password):
            print('4) Include number test - OK')
            security_point += 1
        else:
            print('4) Include number test - FAILED')

        if re.findall('\W+', test_password):
            print('5) Include special symbols test - OK')
            security_point += 2
        else:
            print('5) Include special symbols test - FAILED')

        if re.match(r'\d{2}-\d{2}-\d{4}', test_password) or re.match(
                r'(7|8|\+7)\(\d{3}\)\d{3}-\d{2}-\d{2}', test_password):
            print('6) Include date or phone test - FAILED')
        else:
            print('6) Include date or phone test - OK')
            security_point += 2
    else:
        print('1) Lenght test - FAILED')
    return security_point


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for checking '
                                                 'strenght of password')
    parser.add_argument('<black_list_path>', type=str,
                        help='path of txt file containing blacklist')
    args = parser.parse_args()
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        black_list_path = sys.argv[1]
        password = input('Please, enter your password: ')
        print('Your password strenght is ',
              get_password_strength(password, black_list_path), '(max - 10)')
    else:
        sys.exit('You forget enter path or file does not exist.'
                 'Please read help (--help)')
