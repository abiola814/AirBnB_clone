#!/usr/bin/python3

import cmd
from models.base_model import BaseModel

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

 
if __name__ == '__main__':
    HBNBCommand().cmdloop()
