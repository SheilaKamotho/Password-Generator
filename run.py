from users import User
from credentials import Credentials
import secrets
import string
import pyperclip

# Log in username and password - Done
# Add existing account details - Done
# Create new account credentials - Done
# Random pasword/inputted password - Done
# View various account credentials and the passwords
# Delete credentials
# Copy to clipboard
# Dictate length of password - Done

def create_account(user_name, password):
    '''
    Function that create new  log in account
    '''
    new_user = User(user_name, password)
    return new_user

def save_account(user):
    '''
    Function that saves new account details
    '''
    User.create_account(user)

def login(user_name, password):
    '''
    Function that checks if an account exists and returns details
    '''
    return User.user_exist(user_name, password)

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

def find_credentials(account):
    '''
    A function that finds credentials by account and returns them
    '''

    return Credentials.find_by_account(account)


def check_existing_credentials(account):
    '''
    A function that checks if credentials exists with that account and returns a boolean
    '''


def random_password(psw_len):
    return "".join(secrets.choice(string.ascii_letters+string.digits) for i in range(psw_len))

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

def main():
    print("Hello Welcome to your password app.")
    log_success = False

    while True:
        print("Type r to Register a new user account  or l to Log In into an existing account")
        answer = input().lower()

        if answer == 'r':
            print("Create new account")

            print('Username: ')
            user_name = input()

            print('password: ')
            password = input()
        
            save_account(create_account(user_name, password))
            print(f'Account for {user_name} has been created')

        elif answer == 'l':
            print('Enter Username: ')
            user_name = input()
            print('Enter Password: ')
            password = input()
            log_success = login(user_name, password)if answer == 'l' else False

            while log_success:
                print('Type:\n se to save existing account\n na to create a new account\n dc to display accounts\n del to delete\nlo to log out')

                short_code = input().lower() 
                if short_code == 'na':
                    print('Enter Platform Name ie Twitter')
                    account = input()

                    print('Enter the username:  ')
                    username = input()

                    print('Password: ')
                    print('Enter auto to automatically create password or gen to generate your own password')
                    pw = input().lower()

                    if pw == 'auto':
                        print('Enter your preferred password length')
                        ps_len = int(input())
                        password = random_password(ps_len)
                        print(f'Your new password for {account} is {password}')
                    
                    if pw == 'gen':
                        print('Create password: ')
                        password = input()
                
                elif short_code == 'se':
                    print('Save existing account details')
                    print(' Account:')
                    account = input()

                    print(f'\n username:')
                    username = input()

                    print('\n password:')
                    password = input()

                    save_credentials(create_credentials(account, username, password)) 
                    print(f'{account} username: {username} password: {password} created successfully')
                
                elif short_code == 'dc':
                    if display_credentials():
                        print("Here is a list of all your credentials")
                        print('\n')

                        for Credentials in display_credentials():
                            print(f"{Credentials.account} {Credentials.user_name} .....{Credentials.password}")

                            print('\n')
                    else:
                        print('\n')
                        print("You dont seem to have any accounts saved yet")
                        print('\n')

                elif short_code == 'del':



                    
                    print('Account Deleted')

                elif short_code == 'lo':
                    print('You have logged out')
                    
                else:
                    print('Wrong input')
                    save_credentials(create_credentials(account, username, password))
                    print(f'Account credentials for {account} has been saved, username: {username} password: {password}')
            else: 
                print('Invalid Username or Password')
    else:
        print('Invalid choice')    

if __name__ == '__main__':

    main()