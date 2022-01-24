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