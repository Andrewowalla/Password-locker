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