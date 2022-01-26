import unittest
from credentials import Credentials #importing the credentials class

class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        test case to run before each test case
        '''
        self.new_credentials = Credentials("Youtube", "Mazlaowalla", "des0708")

    def test_save_credentials(self):
        '''
        test case to check if credentials have been added to the credentials list
        '''
        self.new_credentials.save_credentials()  # saving the credentials
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        '''
        test case that does clean up after every test case
        '''

        Credentials.credentials_list = []

    def test_delete_credentials(self):
        '''test case to check if credentials have been deleted from the credentials list'''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Youtube", "Mazlaowalla", "des0708")

        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_display_credentials(self):
        ''' 
        test case to test whether credentials have been displayed 
        '''

        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)

    def test_save_multiple_credentials(self):
        ''' 
        test case to test whether multiple credentials have been saved 
        '''

        self.new_credentials.save_credentials()
        test_multiple = Credentials("Youtube", "Mazlaowalla", "des0708")

        test_multiple.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

