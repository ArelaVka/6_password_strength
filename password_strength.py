import re
import sys
import os
import argparse


def blacklist_test(test_password):
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        with open(sys.argv[1], 'r') as opened_file:
            blacklist = opened_file.read().split()
            if test_password not in blacklist:
                return 1
            else:
                return 0
    else:
            sys.exit('You forget enter path or file does not exist.'
                     'Please read help (--help)')


def length_test(test_password):
    min_length_of_password = 6
    if len(test_password) > min_length_of_password:
        return 1
    else:
        return 0


def case_sensitivity(test_password):
    if re.findall(r'[A-z]', test_password):
        if not (test_password.islower()) or not (test_password.isupper()):
            return 2
    else:
        return 0


def number_test(test_password):
    if re.findall('\d+', test_password):
        return 1
    else:
        return 0


def spec_symbol_test(test_password):
    if re.findall('\W+', test_password):
        return 2
    else:
        return 0


def date_and_phone_test(test_password):
    if not (re.match(r'\d{2}-\d{2}-\d{4}', test_password)) or not (re.match(
            r'\d{2}\.\d{2}\.\d{4}', test_password)) or not (re.match(
            r'(7|8|\+7)\(\d{3}\)\d{3}-\d{2}-\d{2}', test_password)):
        return 2
    else:
        return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for checking '
                                                 'strenght of password')
    parser.add_argument('<black_list_path>', type=str,
                        help='path of txt file containing blacklist')
    args = parser.parse_args()

    password = input('Please, enter your password: ')
    password_strength = 1 + blacklist_test(password) + length_test(
        password) + case_sensitivity(password) + number_test(
        password) + spec_symbol_test(password) + date_and_phone_test(password)
    print('Your password strength is',  password_strength, '(max - 10)')
