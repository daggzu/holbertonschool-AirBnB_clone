#!/usr/bin/python3
"""
Console module for the Holberton Airbnb clone project
"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of a specified class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        new_instance = self.class_dict[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in self.all_objects:
            print("** no instance found **")
            return
        print(self.all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in self.all_objects:
            print("** no instance found **")
            return
        del self.all_objects[key]
        self.save()

    def do_all(self, arg):
        """Prints all instances or instances of a specified class"""
        args = arg.split()
        if len(args) == 0:
            obj_list = list(self.all_objects.values())
        else:
            class_name = args[0]
            if class_name not in self.class_dict:
                print("** class doesn't exist **")
                return
            obj_list = [obj for obj in self.all_objects.values() if obj.__class__.__name__ == class_name]
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in self.all_objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        instance = self.all_objects[key]
        setattr(instance, attr_name, attr_value)
        self.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass

    def precmd(self, line):
        """Hook method executed just before the command is executed"""
        if '.' in line:
            class_name = line.split('.', 1)[0]
            if class_name in self.class_dict:
                line = "{} {}".format(class_name, line.split('.', 1)[1])
        return line

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
