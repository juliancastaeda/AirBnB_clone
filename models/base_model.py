#!/usr/bin/python3
# description of the function
"""
Base Models
"""
""" import """
from datetime import datetime, date, time
import uuid

"""
class BaseModel: attributes/methods
"""
class BaseModel:
    """ Public instance attributes """
    id = str(uuid.uuid4())
    created_at = datetime.now(tz=None)
    updated_at = datetime.now(tz=None)
