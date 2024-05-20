#!/usr/bin/python3
"""Module for the console"""

import cmd
import os
import re
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Console for the app using cmd module"""
    prompt = '(hbnb) '

    def do_create(self, line):
        """Creates a model if argument is valid"""
        if not line:
            print("** class name missing **")
            return
        if line not in storage.classes():
            print("** class doesn't exist **")
            return
        else:
            obj_inst = storage.classes()[line]()
            obj_inst.save()
            print(obj_inst.id)

    def do_show(self, line):
        """Prints the string rep of an instance, class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, line):
        """Prints the string rep of an instance, class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            info = line.split(" ")
            class_name = info[0]
            if class_name in storage.classes():
                if len(info) < 2:
                    print("** instance id missing **")
                else:
                    class_id = info[1]
                    key = f"{class_name}.{class_id}"
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        del storage.all()[key]
                        storage.save()
                        return
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Prints the string rep of all instance"""
        if line and line not in storage.classes():
            print("** class doesn't exist **")
            return
        objects = storage.all()
        if line:
            objects = {k: v for k, v in objects.items() if k.startswith(line)}
        print([str(obj) for obj in objects.values()])

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr_name = args[2]
        attr_val = args[3].strip('"')
        setattr(obj, attr_name, attr_val)
        obj.save()

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

    def precmd(self, line):
        """Handles precommand"""
        if not sys.stdin.isatty():
            line = line.strip()
            print()
        return line

    def do_count(self, class_name):
        """Counts number of instance of a class"""
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        count = sum(1 for obj in storage.all().values()
                    if obj.__class__.__name__ == class_name)
        print(count)

    def default(self, line):
        """Handle <class name>.all() and <class name>.count()"""
        args = line.split('.')
        class_name = args[0]
        if len(args) == 1:
            print(f"*** Unknown syntax: {line}")
            return
        try:
            command = args[1]
            if command == "all()":
                self.do_all(class_name)
            elif command == "count()":
                self.do_count(class_name)
            else:
                match = re.fullmatch(r'show\("(.+)"\)', command)
                destroy_match = re.fullmatch(r'destroy\("(.+)"\)', command)
                if match:
                    obj_id = match.group(1)
                    if class_name in storage.classes():
                        self.do_show(f"{class_name} {obj_id}")
                    else:
                        print("** class doesn't exist **")
                elif destroy_match:
                    obj_id = destroy_match.group(1)
                    if class_name in storage.classes():
                        self.do_destroy(f"{class_name} {obj_id}")
                    else:
                        print("** class doesn't exist **")
                else:
                    print(f"*** Unknown syntax: {line}")
        except IndexError:
            print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
