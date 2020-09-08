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