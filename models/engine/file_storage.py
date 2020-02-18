#!/usr/bin/python3
"""
"""
import json
import os


class FileStorage():
    """comment function"""
    __file_path = 'data.json'
    __objects = {}

    def all(self):
        """function comment"""
        return FileStorage.__objects

    def new(self, obj):
        """function comment"""
        FileStorage.__objects["{}.{}".format(str(type(obj).__class__.__name__),
                       str(obj.id))] = obj

    def save(self):
        """function comment"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            dict = {key: value.to_dict()
                    for key, value in self.__objects.items()}
            json.dump(dict, file)

    def reload(self):
        """ deserialize all the objects """
        try:
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            with open(FileStorage.__file_path, "r") as file:
                obj = json.load(file)
            for value in obj.values():
                self.new(eval(value["__class__"])(**value))
        except:
            pass
