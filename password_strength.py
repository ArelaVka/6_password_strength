def get_passwords_blacklist(path_to_file):
	with open(path_to_file, 'r') as blacklist:
		return blacklist.read().split()


def get_password_strength(password):
    pass


if __name__ == '__main__':
    path_to_blacklist_file = 'blacklist.txt'
    print(get_passwords_blacklist(path_to_blacklist_file))
