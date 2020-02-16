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
    created_at = datetime.now()
    updated_at = datetime.now()
    # created_at = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
    # updated_at = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        """ should print: [BaseModel] str(self.id) self.__dict__ """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime """
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        return self.__dict__
