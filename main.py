
"""
- Deposite money
- Send money
- Account information
- Reset Password
- Exit
"""
#TODO: we will add more functionality to this system. like, user can sent money to another user .
import json
from utils import database
from utils import user


def menu():
    print('Welcome to our money transfer system! (P-pay) ')

    user_input = input("""
        - Create Account. Enter 'C' to Create account
        - Already have account? then press 'L' to login.
        - Press 'E' to Exit
    """)
    while user_input != 'e':

        if user_input.lower() == 'c':
            account_create()
        elif user_input.lower() == 'l':
            login_data()
        else:
            print('Unknown Command! please try again..')

        user_input = input("""
                - Create Account. Enter 'C' to Create account
                - Already have account? then press 'L' to login.
                - Press 'E' to Exit
            """)


def account_create():
    print('Welcome to our app. Please fill up the information below for opening a account. ')
    username = input('Username: ')
    email = input("Email: ")
    phone = int(input("phone: "))
    password = input("password: ")
    data = (username, email, phone, password)
    database.create(*data)
    user.user(name=username, password=password)
    user_choice = input("account successfully created. press 'L' to login now or press 'Q' for main menu. ")

    while user_choice != 'q':
        if user_choice.lower() == 'l':
            login_data()
        else:
            print('Unknown command!. please try again')
        user_choice = input("account successfully created. press 'L' to login now")


def login_data():
    user_name = input('Enter your user name / email: ')
    password = input('Enter your password: ')
    database.login(user_name, password)


menu()
