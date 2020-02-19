#!/usr/bin/python3
# description of the function
import cmd
import models
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    # intro = 'Welcome to the hbnb shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    __class_name = {"BaseModel": BaseModel,
                    "User": User,
                    "Amenity": Amenity,
                    "State": State,
                    "City": City,
                    "Place": Place,
                    "Review": Review}

    # ----- basic hbnb commands -----
    def emptyline(self):
        """ an empty line + ENTER """
        pass

    def do_EOF(self, line):
        """ Exit command to exit the program """
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        # print('Thank you for using hbnb')
        return True

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
            models.storage.save()

    def do_show(self, line):
        """ Prints the string representation of an
        instance based on the class name and id """
        if line is None or line == "":
            print("** class name missing **")
        elif line.split(' ')[0] not in self.__class_name:
            print("** class doesn't exist **")
        elif len(line.split(' ')) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line.split(' ')[0], line.split(' ')[1])
            objects = models.storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                print(objects[key])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        if line is None or line == "":
            print("** class name missing **")
        elif line.split(' ')[0] not in self.__class_name:
            print("** class doesn't exist **")
        elif len(line.split(' ')) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line.split(' ')[0], line.split(' ')[1])
            objects = models.storage.all()
            if key not in objects:
                print("** no instance found **")
            else:
                del objects[key]
                models.storage.save()

    def do_all(self, line):
        """ Prints all string representation of all
        instances based or not on the class name """

        if (len(line.split()) == 0):
            print([str(value) for value in models.storage.all().values()])
            return

        if (line.split()[0] not in self.__class_name):
            print("** class doesn't exist **")
            return

        print([str(value) for key, value in models.storage.all().items()
              if key.split(".")[0] == line])

    def do_update(self, line):
        """  Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file """
        if line is None or line == "":
            print("** class name missing **")
        elif line.split(' ')[0] not in self.__class_name:
            print("** class doesn't exist **")
        elif len(line.split(' ')) < 2:
            print("** instance id missing **")
        elif len(line.split(' ')) < 3:
            print("** attribute name missing **")
        elif len(line.split(' ')) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(line.split(' ')[0], line.split(' ')[1])
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                line_1 = line.split()[2]
                value = line.split()[3]
                setattr(models.storage.all()[key], line_1, value)
                models.storage.save()

    def do_count(self, line):
        """Count command counts the instances of a class"""
        count = 0
        for key, value in models.storage.all().items():
            if key.split(".")[0] == line:
                count += 1
        print(count)

    def default(self, line):
        if (re.match(r"\w+\.\w+(\(\)|\(\"[^\"]*\"(?:, (\"[^\"]*\"|{.*}))*\))",
                     line) is None):
            super().default(line)
            return
        if (line.split(".")[1].split("(")[0] == "all"):
            if (line.split(".")[0] not in self.__class_name):
                print("** class doesn't exist **")
                return

            self.do_all(line.split(".")[0])
        elif (line.split(".")[1].split("(")[0] == "count"):
            if (line.split(".")[0] not in self.__class_name):
                print("** class doesn't exist **")
                return
            self.do_count(line.split(".")[0])
        else:
            super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
