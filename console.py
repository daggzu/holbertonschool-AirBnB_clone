#!/usr/bin/python3
'''Defines the console'''
import json
import cmd
import sys
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command line interpreter, entry point"""
    prompt = '(hbnb) '

    class_dict = {
        "BaseModel": BaseModel
        # Add more classes here
    }

    def do_create(self, arg):
        '''Creates a new instance of a class'''
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        else:
            instance = HBNBCommand.class_dict[arg]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        '''Prints the string representation of an instance'''
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id'''
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        '''Prints all string representation of all instances'''
        args = arg.split()
        obj_list = []
        if not arg:
            for key, obj in storage.all().items():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        else:
            for key, obj in storage.all().items():
                if key.split(".")[0] == args[0]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        '''Updates an instance based on the class name and id'''
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                instance = storage.all()[key]
                setattr(instance, args[2], args[3])
                storage.save()
            else:
                print("** no instance found **")

    def emptyline(self):
        pass

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
