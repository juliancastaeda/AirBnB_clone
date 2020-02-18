#!/usr/bin/python3
# description of the function
"""
Base Models
"""
from datetime import datetime
import uuid
import models
import json


class BaseModel:
    """
    class BaseModel: attributes/methods
    """
    """ Public instance attributes """
    def __init__(self, *args, **kwargs):
        """ """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        """ should print: [BaseModel] str(self.id) self.__dict__ """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """"function comment"""
        dict1 = self.__dict__.copy()
        dict1["__class__"] = type(self).__name__
        dict1["created_at"] = dict1["created_at"].isoformat()
        dict1["updated_at"] = dict1["updated_at"].isoformat()
        return dict1
