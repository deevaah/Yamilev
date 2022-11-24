def login():
    users = {}
    while True:
        log = input('login: ')
        pas = input('password: ')
        getpass = users.get(log)
        if getpass == pas:
            print('Доступ разрешен!')
        elif getpass is None:
            users[log] = pas
            print('Регистрация прошла успешно')
        else:
            print('Доступ запрещен!')

login()
