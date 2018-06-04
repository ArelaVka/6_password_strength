import re
import sys
import os
import getpass


def make_blacklist(path_of_file):
    try:
        with open(path_of_file, 'r') as opened_file:
            return opened_file.read().split()
    except ValueError:
        return None


def blacklist_testing(test_password):
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        blacklist = make_blacklist(sys.argv[1])
        if blacklist:
            if test_password not in blacklist:
                return 1
            else:
                return 0
    else:
        print('You forget enter path or file does not exist. '
              'Blacklist checking is not use!')
        return 0


def length_testing(test_password):
    min_length_of_password = 6
    if len(test_password) > min_length_of_password:
        return 1
    else:
        return 0


def case_sensitivity_testing(test_password):
    if re.search(r'[A-z]', test_password):
        if not (test_password.islower()) or not (test_password.isupper()):
            return 2
    else:
        return 0


def include_number_testing(test_password):
    if re.search('\d+', test_password):
        return 1
    else:
        return 0


def include_spec_symbol_testing(test_password):
    if re.search('\W+', test_password):
        return 2
    else:
        return 0


def include_date_and_phone_testing(test_password):
    if not (re.search('\d{2}-\d{2}-\d{4}', test_password)) or not (re.search(
            '\d{2}\.\d{2}\.\d{4}', test_password)) or not (re.search(
            '(7|8|\+7)\(\d{3}\)\d{3}-\d{2}-\d{2}', test_password)):
        return 2
    else:
        return 0


if __name__ == '__main__':
    password = getpass.getpass(prompt='Enter password to check: ')
    min_password_strength = 1
    if length_testing(password) != 0:
        password_strength = min_password_strength + blacklist_testing(
            password) + length_testing(password) + case_sensitivity_testing(
            password) + include_number_testing(
            password) + include_spec_symbol_testing(
            password) + include_date_and_phone_testing(password)
        print('Your password strength is',  password_strength, '(max - 10)')
    else:
        print('Your password is too weak (length_testing not passed)')
