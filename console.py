#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from datetime import datetime


classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "Place": Place, "City": City, "Amenity": Amenity, "Review": Review}

class HBNBCommand(cmd.Cmd):
    """ Console HBNBCommand class """

    #console display: what shows when you in your program
    prompt = '(hbnb)'


    def do_quit(self, line):
        """ quit to exit the program """
        return True

    def do_EOF(self, line):
        """EOF to exit the program """
        return True

    def emptyline(self):
        """ an empty line + ENTER shouldn’t execute anything """
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel saves it (to the JSON file) and prints the id """
        if __class__.__name__ is None:
            print(' ** class name missing ** ')
            return
        
        try:
            new_base = line + '()'
            instance = eval(new_base)
            print(instance.id)
            instance.save()

        except Exception as f:
            print(' ** class doesn\'t exist ** ')

    def do_show(self, line):
        """ 
            Prints the string representation of an instance
            based on the class name and id
            Ex: $ show BaseModel 1234-1234-1234.
        """
        cmd_line = line.split()
        if len(cmd_line) == 0:
            print("** class name missing **")
            return
        elif cmd_line[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(cmd_line) == 1:
            print("** instance id missing **")
        elif len(cmd_line) == 2:
            instance = cmd_line[0] + "." + cmd_line[1]
            if instance in storage.all():
                print(storage.all()[instance])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
            Deletes an instance based on the class name 
            and id (save the change into the JSON file)
            Ex: $ destroy BaseModel 1234-1234-1234.
        """
        cmd_line = line.split()
        if len(cmd_line) == 0:
            print("** class name missing **")
            return
        elif cmd_line[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(cmd_line) == 1:
            print("** instance id missing **")
        elif len(cmd_line) == 2:
            instance = cmd_line[0] + "." + cmd_line[1]
            if instance in storage.all():
                del storage.all()[instance]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """ 
            Prints all string representation of all instances based or not on the class name. 
            Ex: $ all BaseModel or all
        """
        cmd_line = line.split()
        if len(cmd_line) == 0 or cmd_line[0] == "BaseModel":
            print('["', end="")
            flag = 0
            for obj_id in storage.all().keys():
                if flag == 1:
                    print('", "', end="")
                obj = storage.all()[obj_id]
                print(obj, end="")
                flag = 1
            print('"]')
        elif cmd_line[0] not in classes.keys():
            print("** class doesn't exist **")
        else:
            print('["', end="")
            flag = 0
            len_class = len(cmd_line[0])
            for obj_id in storage.all().keys():
                if obj_id[:len_class] == cmd_line[0]:
                    if flag == 1:
                        print('", "', end="")
                    obj = storage.all()[obj_id]
                    print(obj, end="")
                    flag = 1
            print('"]')

    def do_update(self, line):
        """Updates an instance based on the class name and id
            by adding or updating attribute
            (save the change into the JSON file).
            - Usage:
            update <class name> <id> <attribute name> "<attribute value>"
            - Ex:
            $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
            - Only one attribute can be updated at the time"""
        cmd_line = line.split()
        untouchable = ["id", "created_at", "updated_at"]
        objets = storage.all()
        if not line:
            print("** class name missing **")
        elif cmd_line[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(cmd_line) == 1:
            print("** instance id missing **")
        else:
            instance = cmd_line[0] + "." + cmd_line[1]
            if instance not in storage.all():
                print("** no instance found **")
            elif len(cmd_line) < 3:
                print("** attribute name missing **")
            elif len(cmd_line) < 4:
                print("** value missing **")
            elif cmd_line[2] not in untouchable:
                ojb = objets[instance]
                ojb.__dict__[cmd_line[2]] = cmd_line[3]
                ojb.updated_at = datetime.now()
                ojb.save()

    def do_count(self, line):
        "count instances of the class"

        cmd_line = line.split()

        if cmd_line[0] not in classes:
            return
        else:
            counter = 0
            keys_list = storage.all().keys()
            for search in keys_list:
                len_search = len(cmd_line[0])
                if search[:len_search] == cmd_line[0]:
                    counter += 1
                    # print(search)
            print(counter)
 
if __name__ == '__main__':
    HBNBCommand().cmdloop()
