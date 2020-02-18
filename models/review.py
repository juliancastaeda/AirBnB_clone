#!/usr/bin/python3
"""
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """function comment"""
    def __init__(self, place, user_id, text):
        self.place_id = ''
        self.user_id = ''
        self.text = ''
