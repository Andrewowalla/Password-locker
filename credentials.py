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

    @classmethod
    def display_credentials(cls):
        '''
        display_credentials method that displays credentials in the credentials list
        '''
        return cls.credentials_list

    @classmethod
    def find_by_account(cls, account):
        '''
        find_by_account method that searches objects in the credentials list by account 
        '''

        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials

    @classmethod
    def username_exists(cls, username):
        ''' 
        username_exists method that checks if a username exists 
        '''

        for credentials in cls.credentials_list:
            if credentials.username == username:
                return True
        
        return False
    
