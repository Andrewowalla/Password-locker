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