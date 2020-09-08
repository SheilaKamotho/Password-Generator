from users import User
from credentials import Credentials
import string

# Log in username and password 
# Add existing account details 
# Create new account credentials - random pasword/inputted password 
# View various account credentials and the passwords
# Delete credentials
# Copy to clipboard
# Dictate length of password

def create_account(user_name, password):
    '''
    Function that create new  log in account
    '''
    new_user = User(user_name, password)
    return new_user
def login(user_name, password):
    '''
    Function that checks if an account exists and returns details
    '''
    return User.user_exist(user_name, password)
def save_account(user):
    '''
    Function that saves new account details
    '''
    User.create_account(user)
def create_credentials(account, username, password):
    '''
    A function that creates new credentials
    '''
    new_credentials = Credentials(account, username, password)
    return new_credentials

def display_credentials():
    '''
    A function that returns saved credentials
    '''

    return Credentials.display_credentials()
def save_credentials(credentials):
    '''
    A function that saves credentials
    '''

    credentials.save_credentials()

def delete_credentials(credentials):
    '''
    A function that deletes credentials
    '''
    credentials.delete_credentials()
