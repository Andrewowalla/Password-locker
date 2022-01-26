class User:
    '''
    class that generates new instances of users
    '''
    user_list = [] #empty user list

    def __init__(self, username, password):
        self.userName = userName
        self.password = password 

    def save_user(self):
       '''
       save_user method that saves users in the user list
       '''
       User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method for deleting user in the user list
        '''
        User.user_list.remove(self)

    @classmethod
    def display_users(cls):
        '''
        diplays_users method returns a list of all users in the user list
        '''
        return cls.user_list

    @classmethod
    def verified_users(cls, username, password):
        '''
        method that verifies users that already have an account 
        '''

        for users in cls.user_list:
            if users.username == username and users.password == password:
                return True
            else:
                return False
    
    
