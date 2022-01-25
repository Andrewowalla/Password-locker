import unittest
from user import User #importin the user class

class TestUser(unittest.Testcase):
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
        self.assertEqual(self.new_user.userName"Mazlaowalla")
        self.assertEqual(self.new_user.password"des0708")

if __name__ = '__main__':
    unittest.main()
