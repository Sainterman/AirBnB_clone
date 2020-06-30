#!/usr/bin/python3

import cmd
import sys
class HBNBCommand(cmd.Cmd):
    """

    """

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



console = HBNBCommand()
console.cmdloop()


if __name__ == '__main__':
    pass
