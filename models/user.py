#!/usr/bin/python3
from .base_model import BaseModel

class User(BaseModel):
    """ Represent A User """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
