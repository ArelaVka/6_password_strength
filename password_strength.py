import re


def get_passwords_blacklist(path_to_file):
    with open(path_to_file, 'r') as opened_file:
        return opened_file.read().split()


def get_password_strength(password):
    pass


if __name__ == '__main__':
    security_point = 1
    min_length_of_password = 6
    test_password = input('Please, enter your password: ')
    
    if len(test_password) > min_length_of_password:
        print('1) Lenght test - OK')
        security_point += 1
        print('security_point =', security_point)
    else:
        print('1) Lenght test - FAILED')
        print('security_point =', security_point)
    
    path_to_blacklist_file = 'blacklist.txt'
    blacklist = get_passwords_blacklist(path_to_blacklist_file)
    if test_password in blacklist:
        print('2) Your pass in blacklist - FAILED')
        print('security_point =', security_point)
    else:
        print('2) Blacklist test - OK')
        security_point += 1
        print('security_point =', security_point)
    
    if test_password.islower() or test_password.isupper():
        print('3) Case sensitivity test - FAILED')
        print('security_point =', security_point)
    else:
        print('3) Case sensitivity test - OK')
        security_point += 2
        print('security_point =', security_point)

    if re.findall('\d+', test_password):
        print('4) Include number test - OK')
        security_point += 1
        print('security_point =', security_point)
    else:
        print('4) Include number test - FAILED')
        print('security_point =', security_point)

    if re.findall('\W+', test_password):
        print('5) Include special symbols test - OK')
        security_point += 2
        print('security_point =', security_point)
    else:
        print('5) Include special symbols test - FAILED')
        print('security_point =', security_point)

    if re.match(r'\d{2}-\d{2}-\d{4}', test_password) or re.match(r'(7|8|\+7)\(\d{3}\)\d{3}-\d{2}-\d{2}', test_password):
        print('6) Include date or phone test - FAILED')
        print('security_point =', security_point)
    else:
        print('6) Include date or phone test - OK')
        security_point += 2
        print('security_point =', security_point)

    print('result_security_point =', security_point)
    print(re.match(r'(7|8|\+7)\(\d{3}\)\d{3}-\d{2}-\d{2}', test_password))

