import json
from utils import account_funtionality

file_name = 'login_data.json'


class JsonClass:
    def __init__(self, file):
        self.file_name = file

    def json_load(self):
        with open(self.file_name, 'r+') as file:
            file_content = json.load(file)

        return file_content

    def json_dump(self,):
        with open(self.file_name, 'r+') as file:
            file_content = json.load(file)

        return file_content


files = JsonClass(file_name)


def create(user, email, phone, password):

    program_list = {
           'username': user,
           'email': email,
           'number': phone,
           'password': password,
           'account_balance': None
        }

    with open('login_data.json', 'r+') as file:
        data = json.load(file)
        data.append(program_list)
        file.seek(0)
        json.dump(data, file, indent=2)


def login(user, password):
    # with open('login_data.json', 'r+') as file: #context manager
    #     file_content = json.load(file)

    for _ in files.json_load():
        if _['username'] == user:
            if _['password'] == password:
                print('confirmed user name. ')
                print('confirmed password')
                username = _['username']
                account_funtionality.login_after_menu(username)
                break
    else:
        print('username or password is incorrect')

