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
    
    def test_save_credentials(self):

        '''
        test_save_credentials test case to test if the credentials object is saved into the credentials list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials),1)

    def test_delete_credentials(self):
        '''
        test if we can delete a credential from credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","username","newpass")
        test_credentials.save_credentials()
        
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials),1)

    def test_display_all_credentials(self):
        '''
        test that displays account
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials)
    
    if __name__ == '__main__':
    unittest.main()
