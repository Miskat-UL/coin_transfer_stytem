import json


def create(user, email, phone, password):

    program_list = {
           'username': user,
           'email': email,
           'number': phone,
           'password': password
        }

    with open('login_data.json', 'r+') as file:
        data = json.load(file)
        data.append(program_list)
        file.seek(0)
        json.dump(data, file)


def login(user, password):
    with open('login_data.json', 'r') as file: #context manager
        file_content = json.load(file)

    for _ in file_content:
        if _['username'] == user:
            if _['password'] == password:
                print('confirmed user name. ')
                print('confirmed password')
                username = _['username']
                login_after_menu(username)
                break
    else:
        print('username/ password is incorrect')


def login_after_menu(name):
    print(f'welcome to our service MR. {name}')