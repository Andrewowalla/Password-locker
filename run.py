#!/usr/bin/env python3
from user import User
from credentials import Credentials

def create_account(username, password):
    ''' 
    function to create a new user 
    '''

    new_user = User(username, password)
    return new_user


def create_credentials(account, username, password):
    ''' 
    function to create new credentials 
    '''

    new_credentials = Credentials(account, username, password)
    return new_credentials


def save_user(user):
    ''' 
    function to save user 
    '''

    user.save_user()


def save_credentials(credentials):
    ''' 
    function to save credentials 
    '''

    credentials.save_credentials()


def display_user():
    ''' 
    function that displays users 
    '''

    return User.display_users()


def display_credentials():
    ''' 
    function that displays credentials 
    '''

    return Credentials.display_credentials()


def log_in(user, password):
    ''' 
    function to log in users 
    '''

    verified_user = User.verified_users(user, password)
    return verified_user

def find_credential(account):
    ''' 
    function to find credentials 
    '''

    return Credentials.find_by_account(account)


def generatePassword(stringLength=7):
    """
    Generate a random password string of letters and digits and special characters
    """
    password = string.ascii_uppercase + \
        string.ascii_lowercase + string.digits + "~!@#$%^&*"
    return ''.join(random.choice(password) for i in range(stringLength))

def main():
    print(" ")
    print("*"*50)
    print("Hello..., what is your name?")
    print("*"*50)
    print(" ")

    username = input()

    print(f"Hello {username}. What would you like to do?")
    print('\n')
    while True:
        print("-"*130)
        print(""" Use these short codes
        1. cc - create a new credential
        2. dc - display accounts
        3. lg - login to account
        4. fc - find a credential
        5. d  - delete a credential
        6. gp - generate a password
        7. ex - exit the application""")

        print(" ")
        print("     TYPE IN A SHORT CODE PLEASE")
        print(" ")

        short_code = input().lower()
        if short_code == 'cc':
            print(" ")
            print("-" * 130)
            print("     ***create a new credential***")
            print(" ")
            print("what is your username that you'd like to use?")
            print(" ")
            account = input().lower()
            print("what is the name of the account")
            print(" ")
            user_name = input().lower()
            print("what is the password to your account?")
            print(" ")
            pass_word = input().lower()
            save_user(create_account(account, user_name))
            print('\n')
            save_credentials(create_credentials(
                user_name, pass_word, pass_word))
            print('\n')
            print("-" * 100)
            print(
                f"Your new account { account } { user_name } has been successfully been created")
            print('\n')
        elif short_code == 'dc':
            if display_user():
                print(" ")
                print("User name")
                print(" ")
                print('\n')
                for user in display_user():
                    print(f"{ account }")
                for credentials in display_credentials():
                    print(f"{ pass_word }")
                    print(" ")
            else:
                print('\n')
                print("-" * 130)
                print(" ")
                print("               *** PLESE DO CREATE AN ACCOUNT ***")
                print("                 *** You have not created an account yet ***")
                print(" ")
        elif short_code == 'gp':
            password = generatePassword()
            return password

        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.username} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("The Credential does not exist")
                print('\n')

        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")


        elif short_code == 'lg':
            print('\n')
            print("*" * 30)
            print("Log in to your account")
            print("*" * 30)

            print("Enter your username")
            userName = input().lower()

            print("Enter your password")
            userPassword = input().lower()

            if log_in(userName, userPassword):
                print('\n')
                print("-"*130)
                print(f"Welcome { userName } to your credentials")
                print("-"*130)

                while True:
                    print('''Please choose a short code \n
                        cc - create a new credential
                        dc - display accounts
                        lg - login to account
                        fc - find a credential
                        d  - delete a credential
                        gp - generate a password
                        ex - exit the application''')
                    short_code = input().lower()

                    if short_code == "cc":
                        print('\n')
                        print("New Credential")
                        print("-"*15)

                        print("Type your name...")
                        credential_name = input().lower()

                        print("Type your password")
                        credential_password = input().lower()

                        kuokoa_credentials(create_credentials(
                            credential_name, credential_password))
                        print('\n')
                        print(
                            f"Credentials for *{ credential_name }* has been created and saved successfully")
                        print('\n')

        elif short_code == 'gp':
            print(" ")
            print("     ***TO GENERATE A PASSWORD, ENTER YOUR NAME AND ACCOUNT BELOW")
            print(" ")
            list_of_inputs = [c for c in input()]
            list_of_inputs.reverse()
            print(list_of_inputs)

        elif short_code == "ex":
            print("-"*130)
            print(" ")
            print("         SEE YOU NEXT TIME...")
            print(" ")
            print("-"*130)
            break


if __name__ == '__main__':
    main()