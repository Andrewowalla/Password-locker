import unittest
from user import User #importin the user class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours
    '''
    def setUp(self):
        '''
        setup method to run before each test cases
        '''
        self.new_user = User("Mazlaowalla", "des0708") #create user object

    def test_init(self):
        '''
        test_init to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"Mazlaowalla")
        self.assertEqual(self.new_user.password,"des0708")

    def test_save_user(self):
        '''
        test_save_user test case to check whether a new user has been saved into the user list
        '''

        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self):
        '''
        tear down method that does clean up after each test case
        '''

        User.user_list = []

    def test_delete_user(self):
        '''
        test_delete_user case to check whether a user has been deleted from the user list
        '''

        self.new_user.save_user()
        test_user = User("Mazlaowalla", "des0708")

        test_user.save_user()

        self.new_user.delete_user()  # deleting a user object
        self.assertEqual(len(User.user_list), 1)
    
    def test_display_users(self):
        '''
        test_display_users case to test whether users have been displayed 
        '''

        self.assertEqual(User.display_users(), User.user_list)

if __name__ == '__main__':
    unittest.main()
