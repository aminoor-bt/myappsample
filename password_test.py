def check_passwd(username, password, min_length=8, check_username=True):
    if  len(password) < min_length:
        print('Password is too short')
        return False
    elif check_username and username in password:
        print('pasassword contains username')
        return False
    else:
        print(f'Password for user {username} has passed all checks')
        return True

##FILE
def add_user_to_users_file(user, users_filename='users.txt',min_length=8, check_username=True):
    while True:
        passwd = input(f'Enter password for user {user}: ')
        if check_passwd(user, passwd, min_length, check_username):
            break
    with open(users_filename, 'a') as f:
        f.write(f'{user},{passwd}\n')

add_user_to_users_file('amin')

