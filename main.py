
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


def menu():
    print('Welcome to our money transfer system! (P-pay) ')

    user_input = input("""
        - Create Account. Enter 'C' to Create account
        - Already have account? then press 'L' to login.
        - Press 'E' to Exit
    """)
    while user_input != 'q':

        if user_input == 'c':
            account_create()
        elif user_input == 'l':
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
    user = input('Username: ')
    email = input("Email: ")
    phone = int(input("phone: "))
    password = input("password: ")
    data = (user, email, phone, password)
    database.create(*data)
    user_choice = input("account successfully created. press 'L' to login now")

    while user_choice != 'q':
        if user_choice == 'l':
            login_data()
        else:
            print('Unknown command!. please try again')
        user_choice = input("account successfully created. press 'L' to login now")


def login_data():
    user_name = input('Enter your user name / email: ')
    password = input('Enter your password: ')

    database.login(user_name, password)


menu()