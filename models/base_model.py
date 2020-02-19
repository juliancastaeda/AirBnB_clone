#!/usr/bin/python3
# description of the function :)
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
                if key == 'id':
                    self.id = value
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    if (key != '__class__'):
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        """ should print: [BaseModel] str(self.id) self.__dict__ """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """"function comment"""
        dict1 = self.__dict__.copy()
        dict1["__class__"] = self.__class__.__name__
        dict1["created_at"] = datetime.isoformat(self.created_at)
        dict1["updated_at"] = datetime.isoformat(self.updated_at)
        return dict1

    def delete(self):
        """
        Method to deletes an instance based on the class name
        """
        models.storage.delete(self)
