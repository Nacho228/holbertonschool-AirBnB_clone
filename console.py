#!/usr/bin/python3
"""Console for AirBnB"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple command processor

    Args:
        Cmd: Used to read the input
        and execute a command
    """
    prompt = '(hbnb) '

    def do_help(self, arg: str) -> bool:
        """
        Displays undocumented commands
        """
        return super().do_help(arg)

    def do_EOF(self, line):
        """
        Reaches end of file(quits the program)
        """
        return True

    def do_quit(self, line):
        """
        Exits the program soft, clean and smoothly
        """
        return self.do_EOF

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def do_create(self, line):
        """
        Create a new instance of a specified class.
        """
        args = line.split(" ")
        if not args[0]:
            print("** class name missing **")
            return
        elif line not in storage.class_dict:
            print("** class doesn't exist **")
            return
        else:
            new_obj = storage.class_dict[line]()
            storage.save()
            print(new_obj.id)

    def do_show(self, line):
        """
        Display the string representation of an instance.
        """
        args = line.split(" ")
        if not args[0]:
            print("** class name missing **")
            return
        elif args[0] not in storage.class_dict:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            objs = storage.all()
            coincidence = False
            for key in objs.keys():
                id = key.split(".")
                if id[1] == args[1]:
                    print(objs[key].__str__())
                    coincidence = True
                    break
            if not coincidence:
                print("** no instance found **")
                return

    def do_destroy(self, line):
        """
        Delete an instance based on the class name and instance id.
        """
        args = line.split(" ")
        if not args[0]:
            print("** class name missing **")
            return
        elif args[0] not in storage.class_dict:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            objs = storage.all()
            coincidence = False
            for key in objs.keys():
                id = key.split(".")
                if id[1] == args[1]:
                    del storage.all()[key]
                    storage.save()
                    coincidence = True
                    break
            if not coincidence:
                print("** no instance found **")
                return

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not
        on the class name.
        """
        args = line.split(" ")
        list_objs = []
        if not args[0]:
            for obj in storage.all().values():
                list_objs.append(str(obj))
            print(list_objs)
            return
        elif args[0] in storage.class_dict:
            for key, value in storage.all().items():
                if args[0] in key:
                    list_objs.append(str(value))
            print(list_objs)
            return
        else:
            print("** class doesn't exist **")
            return

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute.
        """
        args = line.split(" ")
        if not args[0]:
            print("** class name missing **")
            return
        elif args[0] not in storage.class_dict:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            objs = storage.all()
            coincidence = False
            for key in objs.keys():
                id = key.split(".")
                if id[1] == args[1]:
                    coincidence = True
                    break
            if not coincidence:
                print("** no instance found **")
                return
            elif len(args) < 3:
                print("** attribute name missing **")
                return
            elif len(args) < 4:
                print("** value missing **")
                return
            else:
                objs[f"{args[0]}.{args[1]}"].__dict__[
                    args[2]] = args[3].strip('"')
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
