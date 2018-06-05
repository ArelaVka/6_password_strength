import re
import sys
import os
import getpass


def load_blacklist(path_of_file):
    try:
        with open(path_of_file, 'r') as opened_file:
            return opened_file.read().split()
    except ValueError:
        return None


def is_in_blacklist(test_password, blacklist):
    return test_password in blacklist if blacklist else False


def check_length(test_password):
    min_length_of_password = 6
    return len(test_password) > min_length_of_password


def has_upper_and_lower_case(test_password):
    return bool(re.search(r'[A-z]', test_password))


def has_number(test_password):
    return bool(re.search('\d+', test_password))


def has_spec_symbol(test_password):
    return bool(re.search('\W+', test_password))


def has_no_date_and_phone(test_password):
    return (not (re.search('\d{2}-\d{2}-\d{4}', test_password)) and
            not (re.search('\d{2}\.\d{2}\.\d{4}', test_password)) and
            not (re.search(
                '(7|8|\+7)\(\d{3}\)\d{3}-\d{2}-\d{2}', test_password))
            )


if __name__ == '__main__':
    password_strength = 1
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        blacklist = load_blacklist(sys.argv[1])
        if blacklist:
            print('Blacklist loading - OK')
    else:
        blacklist = []
        print('Blacklist loading - ERROR ('
              'File is empty or path is not correct)\n'
              'Blacklist check is not use.')

    password = getpass.getpass(prompt='Enter password to check: ')
    if check_length(password):
        password_strength = sum([
            password_strength,
            check_length(password),
            2*has_upper_and_lower_case(password),
            has_number(password),
            2*has_spec_symbol(password),
            not(is_in_blacklist(password, blacklist)),
            2*has_no_date_and_phone(password)]
        )
        print('Your password strength is',  password_strength, '(max - 10)')
    else:
        print('Your password is too short')
