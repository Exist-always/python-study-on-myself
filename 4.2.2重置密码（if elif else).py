password_List = ['*#*#','123456']
def account_Login():
    password = input('Password:')
    password_correct = password == password_List[-1]
    password_reset = password ==password_List[0]
    if password_correct:
        print('Login success!')
    elif password_reset:
        new_password = input('Enter a new password:')
        password_List.append(new_password)
        print('Your password has changed successfully!')
        account_Login()
    else:
        print('Worng password or invalid input!')
        account_Login()
account_Login()
