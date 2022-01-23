import random
import string


class Credentials():

    user_credentials = []

    def __init__(self, account_platform, user_account_username, user_account_password):
        """
            account_platform: New credentials account name eg instagram account.
            user_account_password: New credentials account password.
        """
        self.account_platform = account_platform
        self.user_account_username = user_account_username
        self.user_account_password = user_account_password

        
    def save_credentials(self):
        """
            save credentials method that saves credentials into user_credentials[]
        """
        Credentials.user_credentials.append(self)

    def delete_credentials(self):
        """
            deletes saved credential from the user_credentials[]
        """
        Credentials.user_credentials.remove(self)
