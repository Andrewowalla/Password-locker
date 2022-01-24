class Credentials:
    '''
    class that generates new instances of credentials for users
    '''
    credentials_list = [] #empty credentials list

    def __init__(self, account, username, password):
        self.account : account
        self.username : username
        self.password : password
    
    def save_credentials(self):
        '''
        save_credentials method saves credentials objects to credentials list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes/removes credentials objects in the credentials list
        '''
        Credentials.credentials_list.remove(self)
