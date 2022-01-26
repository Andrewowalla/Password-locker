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

