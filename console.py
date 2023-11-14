#!/usr/bin/env python3
"""This module contains the entry point of the command interpreter"""
# & Import necessary modules and classes
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.engine.file_storage import FileStorage

from models import storage  # & Import the storage object


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class that contains the entry point of the command"""
    # & Set the command prompt
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        Args:
            arg (str): arguments coming from the command line"""
        # & Exit the program
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        Args:
            arg (str): arguments coming from the command line"""
        # & Exit the program
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        # & Do nothing if the line is empty
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file)
        and prints the id
        Args:
            arg (str): <class name>"""
        # & Check if the class name is provided
        if not arg:
            print("** class name missing **")
            return
        # & Check if the class exists
        elif arg not in globals() or not \
                issubclass(globals()[arg], BaseModel):
            print("** class doesn't exist **")
            return
        else:
            # & Create a new instance of the class
            new_instance = globals()[arg]()
            # & Save the new instance
            new_instance.save()
            # & Print the id of the new instance
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of
        an instance based on the class
        name and id
        Args:
            arg (str): <class name> <id>
        """
        # & Split the arguments into a list of strings
        args = arg.split()
        # & Check if the class name is provided
        if len(args) == 0:
            print("** class name missing **")
            return
        # & Check if the class exists and is a subclass of BaseModel
        if args[0] not in globals() or not \
                issubclass(globals()[args[0]], BaseModel):
            print("** class doesn't exist **")
            return
        # & Check if the id is provided
        if len(args) == 1:
            print("** instance id missing **")
            return
        # & Create a key with the class name and id
        key = args[0] + "." + args[1]
        # & Check if the instance exists
        if key in storage.all():
            # & Print the instance
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the
        class name and id (save the change
        into the JSON file)
        Args:
            arg (str): <class name> <id>
        """
        # & Split the arguments into a list of strings
        args = arg.split()
        # & Check if the class name is provided
        if len(args) == 0:
            print("** class name missing **")
            return
        # & Check if the class exists and is a subclass of BaseModel
        if args[0] not in globals() or not \
                issubclass(globals()[args[0]], BaseModel):
            print("** class doesn't exist **")
            return
        # & Check if the id is provided
        if len(args) == 1:
            print("** instance id missing **")
            return
        # & Create a key with the class name and id
        key = args[0] + "." + args[1]
        # & Check if the instance exists
        if key in storage.all():
            # & Delete the instance
            del storage.all()[key]
            # & Save the changes to the JSON file
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of
        all instances based or not on the
        class name
        Args:
            arg (str): <class name>
        """
        # & Split the arguments into a list of strings
        args = arg.split()
        # & If there are no arguments, print all instances
        if len(args) == 0:
            for key, obj in storage.all().items():
                print(obj)
        else:
            # & Check if the class exists and is a subclass of BaseModel
            key = args[0]
            if key not in globals() or not \
                    issubclass(globals()[key], BaseModel):
                print("** class doesn't exist **")
                return
            # & Print all instances of the specified class
            for key, obj in storage.all().items():
                if key.split(".")[0] == args[0]:
                    print(obj)

    def do_update(self, arg):
        """Updates an instance based on the
        class name and id by adding or
        updating attribute (save the change
        into the JSON file)
        Args:
            arg (str): <class name> <id> <attribute name> <attribute value>
        """
        # & Split the arguments into a list of strings
        args = arg.split()
        # & Check if the class name is provided
        if len(args) == 0:
            print("** class name missing **")
            return
        # & Check if the class exists and is a subclass of BaseModel
        if args[0] not in globals() or not \
                issubclass(globals()[args[0]], BaseModel):
            print("** class doesn't exist **")
            return
        # & Check if the id is provided
        if len(args) == 1:
            print("** instance id missing **")
            return
        # & Check if the attribute name is provided
        if len(args) == 2:
            print("** attribute name missing **")
            return
        # & Check if the attribute value is provided
        if len(args) == 3:
            print("** value missing **")
            return
        # & Create a key with the class name and id
        key = args[0] + "." + args[1]
        # & Check if the instance exists
        if key in storage.all():
            # & Update the attribute and save the changes
            setattr(storage.all()[key], args[2], args[3])
            storage.save()
        else:
            print("** no instance found **")


# & Start the command loop
if __name__ == '__main__':
    HBNBCommand().cmdloop()  # & keeps clas in loop
