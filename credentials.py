import random
import string
import pyperclip

class Credentials:

    """
    Class that generates new instances of credentials
    """

    credentials = []

    def __init__(self, account, username, password):

        '''
        __init__ method that helps us define properties for our objects.
        
        Args:
            account: New credentials account name.
            username : New credentials password.
            password: New credentials password.
           
        '''

        self.account = account
        self.username = username
        self.password = password
    
    def save_credentials(self):

        '''
        Method saves credentials objects into credentials list
        '''

        Credentials.credentials.append(self)
    
    def delete_credentials(self):

        '''
        Method deletes a saved credential
        '''
        Credentials.credentials.remove(self)

    @classmethod
    def find_account(cls, account):
        '''
        Method that takes in an account and returns credentials.
        '''
        for Credentials in cls.credentials:
            if Credentials.account == account:
                return Credentials

    @classmethod
    def credentials_exist(cls, account):
        ''' 
        Method that checks if an acount credential exists and returns a boolean
        '''
        for Credentials in cls.credentials:
            if Credentials.account == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
         
        '''
        Method that displays credentials list
        '''
        return cls.credentials

