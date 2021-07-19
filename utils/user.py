from utils import account_funtionality
import json
file_name = 'user_account_data.json'


class JsonClass:
    def __init__(self, file):
        self.file_name = file

    def json_load(self):
        with open(self.file_name, 'r+') as file:
            file_content = json.load(file)

        return file_content


files = JsonClass(file_name)


def user(name, password):
    usd = int(input('Add some money to your wallet now:  '))
    user_action = {
        "username": name,
        "passsword": password,
        "total_money": usd,

    }

    with open('user_account_data.json', 'r+') as file:
        data = json.load(file)
        data.append(user_action)
        file.seek(0)
        json.dump(data, file, indent=2)


def account_details(name):
    for _ in files.json_load():
        if _['username'] == name:
            print(
                f"""
                username:{_['username']}
                Email: {_['email']} 
                """
            )

    # login_after_menu(name)


def send_money(name):
    for item in files.json_load():
        if item['username'] == name:
            acc_balance = item["total_money"]
    retrive_info(balance=acc_balance)


def retrive_info(balance):
    send_person = input("Receiver name: ")
    send_amount = int(input("Enter amount you want to send: "))
    print(f"your balance {balance}")

    for info in files.json_load():
        json_data = files.json_load()
        if info['username'] in send_person:
            print("person found")
            print("sending money on process............")
            info['total_money'] += send_amount
            with open('user_account_data.json', 'r+') as file:
                json.dump(json_data, file, indent=2)
            break
    else:
        print("sorry user not found..")





def deposit_money(name):
    pass

