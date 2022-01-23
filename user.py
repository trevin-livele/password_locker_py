class User():

     user_accounts = []
     def __init__(self, first_name, last_name, username, password):
         
        """
        Initialize the user.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password


     def save_user(self):
        """
        Save user to list.
        """
        User.user_accounts.append(self)


     def delete_user(self):
        """ 
        Delete user from the list
        """
        User.user_accounts.remove(self)