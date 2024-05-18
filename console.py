#!/usr/bin/python3
"""Module for the console"""

import cmd
import os
import re
import sys
from models import storage
from models import *


class HBNBCommand(cmd.Cmd):
    """Console for the app using cmd module"""
    prompt = "(hbnb)"

    def do_create(self, line):
        """Creates a model if argument is valid"""
        if line != "" or line is not None:
            if line not in storage.classes():
                print("** class doesn't exist **")
            else:
                obj_inst = storage.classes()[line]()
                obj_inst.save()
                print(obj_inst.id)
        else:
            print("** class name missing **")

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
