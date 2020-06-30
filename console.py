#!/usr/bin/python3

import cmd
import sys
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """

    """
    clases = ["BaseModel"]

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_help(self, arg):
        """
        default help

        """
        if arg == 'quit':
            print("quit command to exit the program")
        else:
            cmd.Cmd.do_help(self, arg)

    def do_quit(self, arg):
        """
        Exit CLI
        """
        sys.exit(1)

    def do_EOF(self, arg):
        """
        handle EOF
        """
        sys.exit(1)

    def help_EOF(self):
        print("Hit Ctrl-D to exit, means EOF")

    def help_help(self):
        print("type help <command>")

    def do_create(self, line):
        """
        Create a new instance of BaseModel
        and saves to JSON file
        """
        args = line.split()
        if len(args) != 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.clases:
            print("** class doesn't exist **")
        else:
            new = eval(args[0]+'()')
            models.storage.save()
            print(new.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
