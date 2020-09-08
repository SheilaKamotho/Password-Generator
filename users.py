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

    def create_account(self):
        User.users.append(self)

    @classmethod
    def user_exist(cls, user_name, password):

        '''
        Method that checks if a user exists and returns a boolean
        '''
        for user in cls.users:
            if user.user_name == user_name and user.password == password:
                return True
        return False




        