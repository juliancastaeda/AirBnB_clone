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
        if kwargs != {} and kwargs is not None:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value,
                            '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == '__class__':
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            # models.storage.save()
    # created_at = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
    # updated_at = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        """ should print: [BaseModel] str(self.id) self.__dict__ """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime """
        self.updated_at = datetime.now()
        # models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """"function comment"""
        dict1 = self.__dict__.copy()
        dict1["__class__"] = str(type(self).__class__.__name__)
        if "created_at" in dict1:
            dict1['created_at'] = dict1['created_at'].isoformat()
        if "updated_at" in dict1:
            dict1['updated_at'] = dict1['updated_at'].isoformat()
        return dict1
