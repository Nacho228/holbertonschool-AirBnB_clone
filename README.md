**# AirBnB Clone - Command Interpreter**

This is the first step towards building an AirBnB clone, a web application that allows management of AirBnB objects.

The command interpreter allows for the following functionalities:
- Creation of new objects (User, State, City, Place)
- Retrieval of objects from a file, database, etc.
- Operations on objects (counting, computing stats)
- Updating attributes of an object
- Destruction of an object

**Usage:**

The command interpreter provides an interactive mode where commands can be entered one by one, or a non-interactive mode where commands can be piped in.

**Interactive Mode**

To start the command interpreter in interactive mode, run the following command:

    $ ./console.py

Once the interpreter starts, the prompt (hbnb) will be displayed. You can then enter commands and press Enter to execute them.

**Non-Interactive Mode**

To use the command interpreter in non-interactive mode, you can pipe a series of commands into the interpreter.

Example:

$ echo "help" | ./console.py

This will execute the command "help" in the command interpreter.

Available Commands

The command interpreter supports the following commands:
- help: Displays the list of available commands or provides help for a specific command.
- quit: Exits the command interpreter.
- create: Creates a new instance of a specified class.
- show: Displays the string representation of an instance based on the class name and instance ID.
- destroy: Deletes an instance based on the class name and instance ID.
- all: Displays the string representation of all instances or all instances of a specified class.
- update: Updates the attributes of an instance based on the class name and instance ID.

Example:
```
$ ./console.py
(hbnb) help    # Displays available commands 

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create BaseModel    # Creates an instance of BaseModel class

1256552c-6f81-40f0-8463-5016c460c90d

(hbnb) show BaseModel 1256552c-6f81-40f0-8463-5016c460c90d    # Shows the instance created, looking for its ID.

[BaseModel] (1256552c-6f81-40f0-8463-5016c460c90d) {'id': '1256552c-6f81-40f0-8463-5016c460c90d', 'created_at': datetime.datetime(2023, 7, 9, 14, 0, 36, 649919),
'updated_at': datetime.datetime(2023, 7, 9, 14, 0, 36, 649919)}

(hbnb) create Amenity    # Creates a instance of Amenity.

62375f62-cb49-4d66-acb3-5175e0c8703d

(hbnb) update Amenity 62375f62-cb49-4d66-acb3-5175e0c8703d id 23    # Updates the instance based on the class name and the ID

(hbnb) show Amenity 62375f62-cb49-4d66-acb3-5175e0c8703d

[Amenity] (23) {'id': '23', 'created_at': datetime.datetime(2023, 7, 9, 14, 3, 30, 698780), 'updated_at': datetime.datetime(2023, 7, 9, 14, 3, 30, 698780)}

(hbnb) all    # Displays all instances created until now

["[BaseModel] (1256552c-6f81-40f0-8463-5016c460c90d) {'id': '1256552c-6f81-40f0-8463-5016c460c90d', 'created_at': datetime.datetime(2023, 7, 9, 14, 0, 36, 649919), 
'updated_at': datetime.datetime(2023, 7, 9, 14, 0, 36, 649919)}", "[Amenity] (23) {'id': '23', 'created_at': datetime.datetime(2023, 7, 9, 14, 3, 30, 698780), 
'updated_at': datetime.datetime(2023, 7, 9, 14, 3, 30, 698780)}"]

(hbnb) quit    # Ends the program

$
```
File Storage
The command interpreter uses file storage to persist data. The objects are serialized and deserialized to/from JSON format and stored in files.

The file storage is implemented in the file_storage.py module.

Testing

The project includes unit tests to validate the implementation of all classes and the file storage engine. The tests are located in the tests directory and can be executed using the following command:

python3 -m unittest discover tests

or you can test in non-interactive mode with this command: 

$ echo "python3 -m unittest discover tests" | bash

Authors
- Gabriel Acosta
- Ignacio Llanes
