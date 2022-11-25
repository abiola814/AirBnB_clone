#!usr/bin/python3
""" BaseModel class"""

import uuid
from datetime import datetime
from models import storage
#datetime format
dtm = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """ 
        Initializing the BaseModel...
        Create a public instance attributes eg. id in string, created_at and updated_at
    """
    def __init__(self, *args, **kwargs):

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

                self.created_at = datetime.strptime(kwargs["created_at"], dtm)

            if hasattr(self, 'updated_at') and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], dtm)

        else:
            self.id = str(uuid.uuid4())  #Generates a Random id everytime an instance is created
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        return self.__class__.__name__, self.id, self.__dict__

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        n_dict = self.__dict__.copy()
        n_dict["created_at"] = n_dict["created_at"].strftime(dtm)
        n_dict["updated_at"] = n_dict["created_at"].strftime(dtm)
        n_dict["__class__"] = self.__class__.__name__
        return n_dict
