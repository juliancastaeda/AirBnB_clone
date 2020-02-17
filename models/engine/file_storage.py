#!/usr/bin/python3
"""
"""
import json
import models
import models.base_model
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
        keys = (obj.__class__.__name__,obj.id)
        FileStorage.__objects[keys] = obj

    def save(self):
        """function comment"""
        with open(FileStorage.__file_path, 'w') as file:
            dict2 = {k: value.to_dict() for (key, value) in FileStorage.__objects.items()}
            file.write(json.dump(dict, file)
            
    def reload(self):
        """ deserialize all the objects """
        try:
            from models.base_model import BaseModel
            with open(FileStorage.__file_path, "r") as file:
                obj = json.load(file)
                for v in obj.values():
                    self.new(eval(v["__class__"])(**v))
        except IOError:
            pass
