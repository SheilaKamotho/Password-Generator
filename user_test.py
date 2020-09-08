import unittest
from users import User

class TestUsers(unittest.TestCase):
    '''
    Test class that defines test cases for the users class behaviours.
    '''
    def tearDown(self):

        '''
        tearDown method to run after each test case.
        '''

    User.users = []
    def setUp(self):

        '''
        Set up method to run before each test cases.
        '''

        self.new_user = User("Sheila", "SheeKam") 