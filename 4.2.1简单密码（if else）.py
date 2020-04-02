def account_login():
    password = input('password:')
    if password == '123456':
        print('Login success!')
    else:
        print('Wrong password or invalid input!')
        account_login()
account_login()
#简单密码