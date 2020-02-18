#!/usr/bin/python3
"""

"""
from models.base_model import BaseModel


class User(BaseModel):
    """function comment"""
    def __init__(self, email, password, first_name, last_name):
        """function comment"""
        self.email = ''
        self.password = ''
        self.first_name =''
        self.last_name = ''
