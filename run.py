import unittest 
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):
    def tearDown(self):

        '''
        tearDown method run after each test cases.
        '''
        Credentials.credentials=[]

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Twitter","Sheila","Sheekam")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account,"Twitter")
        self.assertEqual(self.new_credentials.username,"Sheila")
        self.assertEqual(self.new_credentials.password,"Sheekam")
