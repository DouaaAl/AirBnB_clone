#!/usr/bin/python3

    """
    
    """
import cmd

class HBNBCommand(cmd.Cmd):
    """

    """
    prompt = "(hbnb)"
    def do_quit(self, arg):
    """

    """

    return true
    
    def help_quit(self, arg):
    """

    """
    print("Quit command to exit the programm")
    
    def do_EOF(self, arg):
    """

    """
    print()
    return true

if __name__ = "__main__":
    
    HBNBcommand().cmdloop
