#!/usr/bin/env python3.8
from user import User
from credentials import Credentials



def create_new_user(first_name, last_name, username, user_password):  # create a new user
    '''
    create a new user
    '''
    new_user = User(first_name, last_name, username, user_password)
    return new_user



def save_user(user):  # save user
    '''
    save user
    '''
    return user.save_user()

def delete_user(username):  # delete user
    '''
    delete user
    '''
    return User.delete_user(username)


def check_existing_user(username):  # check if the user exists
    '''
    check if user exists
    '''
    return User.user_exist(username)


def check_user_password(username, password):  # check if the password is correct
    '''
    funtion to check whether the user enter the correct username and password
    '''
    return User.check_user(username, password)



# create new credential
def create_new_credential(account_name, account_username, account_password):
    '''
    function to create a new credential
    '''
    new_credential = Credentials(
        account_name, account_username, account_password)
    return new_credential