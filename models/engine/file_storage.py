#!/usr/bin/python3
""" FileStorage class """

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

sub_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                "Place": Place, "City": City, "Amenity": Amenity, "Review": Review}


class FileStorage:
    """  serializes instances to a JSON file and deserializes JSON file to instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in the obj with key <obj classclasses name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """ 
        json_obj = {}
        for key,objects in self.__objects.items():
            json_obj[key] = objects.to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            json.dump(json_obj, file)

    def reload(self):
        """deserializes the JSON file to __objects """
        #only if the JSON file (__file_path) exists
        #otherwise, do nothing. If the file doesn’t exist
        #no exception should be raised
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as file:
                jn = json.load(file)
            for key, data in jn.items():
                obj = sub_classes[data['__class__']](**data)
                self.__objects[key] =obj
        except FileNotFoundError:
            pass
