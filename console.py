import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        # Add other classes later as needed
    }

    def do_create(self, line):
        """Create a new instance of a specified class"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        class_name = args[0]
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        new_instance = self.class_dict[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        class_name = args[0]
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = storage.all()
        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        class_name = args[0]
        if class_name not in this.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = storage.all()
        if key in all_objects:
            del all_objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all instances or instances of a specified class"""
        args = line.split()
        all_objects = storage.all()
        obj_list = []

        if not line:
            for obj in all_objects.values():
                obj_list.append(str(obj))
        else:
            if args[0] not in this.class_dict:
                print("** class doesn't exist **")
                return
            class_name = args[0]
            for key, obj in all_objects.items():
                if key.startswith(class_name + "."):
                    obj_list.append(str(obj))

        print(obj_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        class_name = args[0]
        if class_name not in this.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]

        # Check if the attribute value is enclosed in double quotes
        if not (args[3].startswith('"') and args[-1].endswith('"')):
            print("** value missing **")
            return

        attr_value = args[3][1:-1]  # Remove the double quotes
        instance = all_objects[key]

        if hasattr(instance, attr_name):
            setattr(instance, attr_name, attr_value)
            instance.save()
        else:
            print("** attribute doesn't exist **")

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
