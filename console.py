#!/usr/bin/python3
"""
Modules handles custom CLI connected to file storage
"""
import cmd
import sys
import models
import shlex
import json
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Console a program called console.py that contains
        the entry point of the command interpreter.
    """
    clases = ["BaseModel", "User", "Amenity", "Place",
              "City", "State", "Review"]

    msgs_error = {
        1: "** class name missing **",
        2: "** class doesn't exist **",
        3: "** instance id missing **",
        4: "** no instance found **",
        5: "** value missing **"
    }

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
            print("{}".format(self.msgs_error[1]))
        elif args[0] not in HBNBCommand.clases:
            print("{}".format(self.msgs_error[2]))
        else:
            new = eval(args[0]+'()')
            models.storage.save()
            print(new.id)

    def do_show(self, line):
        """ Prints the string representation of an
            instance based on the class name and id.
        """
        args = line.split()
        if line == "":
            print("{}".format(self.msgs_error[0]))
        elif args[0] not in HBNBCommand.clases:
            print("{}".format(self.msgs_error[1]))
        elif len(args) < 2:
            print("{}".format(self.msgs_error[2]))
        else:
            date = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            try:
                obj = date[key]
                print(obj)
            except KeyError:
                print("{}".format(self.msgs_error[3]))

    def do_destroy(self, line):
        """ Deletes an instance based on the class name
            and id (save the change into the JSON file).
        """
        args = line.split()
        if line == "":
            print("{}".format(self.msgs_error[0]))
        elif args[0] not in HBNBCommand.clases:
            print("{}".format(self.msgs_error[1]))
        elif len(args) < 2:
            print("{}".format(self.msgs_error[2]))
        else:
            date = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in date:
                del date[key]
                storage.FileStorage.__objects = date
                storage.save()
                return
            print("{}".format(self.msgs_error[3]))

    def do_all(self, line=""):
        """ Prints all string representation of all
            instances based or not on the class name.
        """
        date = models.storage.all()
        if line == "":
            for instance_key, instance_obj in date.items():
                print(instance_obj)
        else:
            args = line.split()
            if args[0] not in HBNBCommand.clases:
                print("{}".format(self.msgs_error[1]))
            else:
                for instance_key, instance_obj in date.items():
                    obj = instance_obj.to_dict()
                    if obj["__class__"] == args[0]:
                        print(instance_obj)

    def do_update(self, line=""):
        """ Updates an instance based on the class name
            and id by adding or updating attribute
            (save the change into the JSON file).
        """
        date = models.storage.all()
        args = line.split()
        if not line:
            print("{}".format(self.msgs_error[0]))
        elif args[0] not in HBNBCommand.clases:
            print("{}".format(self.msgs_error[1]))
        elif len(args) < 2:
            print("{}".format(self.msgs_error[2]))
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in date:
                if len(args) < 3:
                    print("{}".format(self.msgs_error[4]))
                elif len(args) < 4:
                    print("{}".format(self.msgs_error[5]))
                else:
                    obj = date[key]
                    setattr(obj, args[2], args[3])
            else:
                print("{}".format(self.msgs_error[3]))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
