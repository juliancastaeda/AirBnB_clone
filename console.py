#!/usr/bin/python3
# description of the function
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to the hbnb shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    # ----- basic hbnb commands -----
    def do_EOF(self, line):
      """ Exit command to exit the program """
      return True

    def do_quit(self, line):
      """ Quit command to exit the program """
      print('Thank you for using hbnb')
      return True

    def emptyline(self):
      """ an empty line + ENTER """
      pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
