#!/usr/bin/python3
"""Module for the console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Console for the app using cmd module"""
    prompt = "(hbnb)"

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