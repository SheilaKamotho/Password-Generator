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

    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name, "Sheila")
        self.assertEqual(self.new_user.password, "SheeKam")

    def test_create_account(self):
        '''
        test if the user object is saved into the user list
        '''
        self.new_user.create_account()
        self.assertEqual(len(User.users), 1)
  
if __name__ == '__main__':
    unittest.main()