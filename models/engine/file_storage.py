#!/usr/bin/python3
"""
"""
import json
import os
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage():
    """comment function"""
    __file_path = 'data.json'
    __objects = {}
    __class_name = {"BaseModel": BaseModel, "User": User,
                    "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

    def all(self):
        """function comment"""
        return FileStorage.__objects

    def new(self, obj):
        """function comment"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """function comment"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            dict = {key: value.to_dict()
                    for key, value in FileStorage.__objects.items()}
            json.dump(dict, file)

    def reload(self):
        """ deserialize all the objects """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                dicts = json.load(file)
            for key, value in dicts.items():
                line = key.split(".")[0]
                if line in FileStorage.__class_name:
                    self.__objects[key] = self.__class_name[line](**value)
        except FileNotFoundError:
            pass
