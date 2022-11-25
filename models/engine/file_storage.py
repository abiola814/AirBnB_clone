#!/usr/bin/python3
""" FileStorage class """

import json

class FileStorage:
    """  serializes instances to a JSON file and deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """ 
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
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
        except FileNotFoundError:
            pass
