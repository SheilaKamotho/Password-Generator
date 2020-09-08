class User:

    """
    Class that generates new instances of users
    """
    
    users = []

def __init__(self, user_name, password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
        user_name: new account username
        password: new account password
        '''
        self.user_name = user_name
        self.password = password