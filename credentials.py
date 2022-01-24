class Credentials:
    '''
    class that generates new instances of credentials for users
    '''
    credentials_list = [] #empty credentials list

    def __init__(self, account, username, password):
        self.account : account
        self.username : username
        self.password : password
        