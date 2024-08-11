#!/usr/bin/python

"""
creating user class"
"""
from models.base_models import BaseModel

class User(BaseModel):
    """
    new class

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
