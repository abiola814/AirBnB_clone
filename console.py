#!/usr/bin/python3

import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
