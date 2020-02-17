#!/usr/bin/python3
# description of the function
import cmd
from models.base_model import BaseModel
# from models import storage
import models

class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to the hbnb shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    __class_name = {"BaseModel": BaseModel}

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

    def do_create(self, line):
        """ Creates a new instance of BaseModel """
        if line is None or line == "":
            print("** class name missing **")
        elif line not in self.__class_name:
            print("** class doesn't exist **")
        else:
            new_model = self.__class_name[line]()
            new_model.save()
            print(new_model.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
