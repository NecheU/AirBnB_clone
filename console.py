#!/usr/bin/python3
"""Module for the console"""

import cmd
from models import *

class HBNBCommand(cmd.Cmd):
    """Console for the app using cmd module"""
    prompt = "(hbnb)"

    def do_create(self, line):
        """Creates new instance of BaseModel"""
        if len(line) < 2:
            print("** class name missing **")
        else:
            arg = line.split()
            print(f"{arg}")
            if arg == BaseModel:
                storage = base_model.BaseModel()
                storage.save()
                print(storage.id)
            else:
                print("** class doesn't exist **")

    def do_quit(self, line):
        """Exits the program"""
        return True

    def do_EOF(self, line):
        """Exits the program"""
        return True

    def emptyline(self):
        """Handles an empty line"""
        pass
        # return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
