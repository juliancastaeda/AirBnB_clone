#!/usr/bin/python3
# description of the function
"""
Base Models
"""
from datetime import datetime
import uuid



class BaseModel:
    """
    class BaseModel: attributes/methods
    """
    """ Public instance attributes """
    id = str(uuid.uuid4())
    created_at = datetime.now(tz=None)
    updated_at = datetime.now(tz=None)

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        """ should print: [BaseModel] str(self.id) self.__dict__ """
        return "[()] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
