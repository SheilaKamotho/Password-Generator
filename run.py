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