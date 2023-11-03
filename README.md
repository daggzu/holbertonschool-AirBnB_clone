# Holbertonschool-AirBnB_Clone

## Authors

|Diego Gonzalez- [GitHub](https://github.com/daggzu) /[Email](diegog8603@gmail.com)|
|Omar Velez - [GitHub](https://github.com/Natzu83)| / [LinkedIn](https://www.linkedin.com/in/omar-velez-749012175/)| / [Email](natzuac@yahoo.com)|

## AirBnb Console - Project's Intention

A bare bones console created to clone the AirBnb console this project is similar to the simple shell we did via
the C Language, we are creating a command
interpreter that works in similar fashion but is
limited to specific use-cases.

Use-cases our project will be able to manage:

- Create new objects (ex: new User or a new
  Place).
- Retrieve an object from a file, a database, etc.
- Do operations on objects (count, compute stats,
  etc).
- Update attributes of an object.
- Destroy an object.

## Flowchart

![flowairjpeg](https://github.com/Natzu83/holbertonschool-zero_day/assets/130172504/00e62d49-8dab-40a4-9b50-ea72f62acce8)


## Learning Objectives

| Objective                                                          | Description                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| How to create a Python package                                     | A Python package is a way of organizing related modules into a directory hierarchy. It involves creating a directory, placing related modules inside it, and adding an `__init__.py` file.                                                                            |
| How to create a command interpreter in Python using the cmd module | The `cmd` module in Python provides a framework for building line-oriented command interpreters. It can be used to build interactive shells and other command interpreters.                                                                                           |
| What is Unit testing and how to implement it in a large project    | Unit testing is a method of software testing that checks whether individual components of the source code are working correctly. It involves writing test cases for each function or method in your code and running them to ensure they produce the expected output. |
| How to serialize and deserialize a Class                           | Serialization is the process of converting a data structure or object state into a format that can be stored or transmitted and reconstructed later. In Python, you can use the `pickle` module for serialization and deserialization.                                |
| How to write and read a JSON file                                  | JSON (JavaScript Object Notation) is a popular data format with diverse uses in data interchange, including that of web applications with servers. In Python, you can use the `json` module to read and write JSON files.                                             |
| How to manage datetime                                             | The `datetime` module in Python is used for dealing with dates and times. It provides classes for manipulating dates and times in a simple and complex way.                                                                                                           |
| What is an UUID                                                    | UUID (Universally Unique Identifier) is a python library which helps in generating random objects of 128 bits as ids. It provides the uniqueness as it generates ids on the basis of time, Computer hardware (MAC etc.).                                              |
| What is \*args and how to use it                                   | `*args` in Python is used to pass a variable number of non-keyworded arguments to a function. It allows you to pass any number of positional arguments to the function.                                                                                               |
| What is \*\*kwargs and how to use it                               | `**kwargs` in Python is used to pass a variable number of keyworded arguments to a function. It allows you to pass any number of keyword arguments to the function.                                                                                                   |
| How to handle named arguments in a function                        | Named arguments, also known as keyword arguments, are used in function calls. They allow the caller to specify the argument name along with its value, making it easier to understand what value is being passed for which function parameter.                        |

# Program's Usage: `./console.py`

## Interactive Mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
2f13f0f8-bb77-41e7-ba5a-21308e8aca38
(hbnb) all BaseModel
[BaseModel] (123) {'id': '123', 'created_at': datetime.datetime(2023, 11, 1, 16, 22, 1, 372753), 'updated_at': datetime.datetime(2023, 11, 1, 16, 22, 1, 372757)}
[BaseModel] (2f13f0f8-bb77-41e7-ba5a-21308e8aca38) {'id': '2f13f0f8-bb77-41e7-ba5a-21308e8aca38', 'created_at': datetime.datetime(2023, 11, 2, 7, 50, 4, 191300), 'updated_at': datetime.datetime(2023, 11, 2, 7, 50, 4, 191353)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 2f13f0f8-bb77-41e7-ba5a-21308e8aca38 first_name "Bety"
(hbnb) show BaseModel 2f13f0f8-bb77-41e7-ba5a-21308e8aca38
[BaseModel] (2f13f0f8-bb77-41e7-ba5a-21308e8aca38) {'id': '2f13f0f8-bb77-41e7-ba5a-21308e8aca38', 'created_at': datetime.datetime(2023, 11, 2, 7, 50, 4, 191300), 'updated_at': datetime.datetime(2023, 11, 2, 7, 50, 4, 191353), 'first_name': '"Bety"'}
(hbnb) create BaseModel
11ed04a1-a79a-48de-9d6b-f9cb099491ae
(hbnb) all BaseModel
[BaseModel] (123) {'id': '123', 'created_at': datetime.datetime(2023, 11, 1, 16, 22, 1, 372753), 'updated_at': datetime.datetime(2023, 11, 1, 16, 22, 1, 372757)}
[BaseModel] (2f13f0f8-bb77-41e7-ba5a-21308e8aca38) {'id': '2f13f0f8-bb77-41e7-ba5a-21308e8aca38', 'created_at': datetime.datetime(2023, 11, 2, 7, 50, 4, 191300), 'updated_at': datetime.datetime(2023, 11, 2, 7, 50, 4, 191353), 'first_name': '"Bety"'}
[BaseModel] (11ed04a1-a79a-48de-9d6b-f9cb099491ae) {'id': '11ed04a1-a79a-48de-9d6b-f9cb099491ae', 'created_at': datetime.datetime(2023, 11, 2, 7, 52, 45, 62503), 'updated_at': datetime.datetime(2023, 11, 2, 7, 52, 45, 62552)}
(hbnb) destroy Basemodel 2f13f0f8-bb77-41e7-ba5a-21308e8aca38
** class doesn't exist **
(hbnb) destroy BaseModel 2f13f0f8-bb77-41e7-ba5a-21308e8aca38
(hbnb) show BaseModel 2f13f0f8-bb77-41e7-ba5a-21308e8aca38
** no instance found **
(hbnb)
(hbnb)
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```

## Non-Interactive Mode

```bash
$ echo "create BaseModel" | ./console.py
1234-1234-1234
$

$ echo "show BaseModel 1234-1234-1234" | ./console.py
[BaseModel] (1234-1234-1234) {'id': '1234-1234-1234', 'created_at': '2023-11-01T16:22:01.372753', 'updated_at': '2023-11-01T16:22:01.372757'}
$


$ echo "destroy BaseModel 1234-1234-1234" | ./console.py
$

$ echo "all BaseModel" | ./console.py
[]
$
```

# Project Structure:

| File/Folder                      | Description                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| `AUTHORS`                        | Contains information about the authors of the project.                                |
| `console.py`                     | Contains the main entry point of the command interpreter.                             |
| `file.json`                      | This file is used to store all objects.                                               |
| `__init__.py`                    | Makes the folder a Python module.                                                     |
| `models/`                        | This folder contains all the classes used in this project.                            |
| `README.md`                      | This is the file you are currently reading, contains information about this project.  |
| `test_base_model_dict.py`        | Contains the unit tests for the `BaseModel` class (dictionary representation).        |
| `test_base_model.py`             | Contains the unit tests for the `BaseModel` class.                                    |
| `tests/`                         | This folder contains all the unit tests for the project.                              |
| `test_save_reload_base_model.py` | Contains the unit tests for the `save` and `reload` methods of the `BaseModel` class. |
| `test_save_reload_user.py`       | Contains the unit tests for the `save` and `reload` methods of the `User` class.      |
| `.gitignore`                     | This file contains a list of files that should be ignored by git.                     |

## Models/:

| File/Folder     | Description                                                                              |
| --------------- | ---------------------------------------------------------------------------------------- |
| `amenity.py`    | Contains the `Amenity` class.                                                            |
| `base_model.py` | Contains the `BaseModel` class, the parent class for all other classes.                  |
| `city.py`       | Contains the `City` class.                                                               |
| `engine/`       | This folder contains the storage engine for the project.                                 |
| `__init__.py`   | Makes the folder a Python module.                                                        |
| `place.py`      | Contains the `Place` class.                                                              |
| `__pycache__/`  | This folder contains Python3 byte code files that are automatically generated by Python. |
| `review.py`     | Contains the `Review` class.                                                             |
| `state.py`      | Contains the `State` class.                                                              |
| `user.py`       | Contains the `User` class.                                                               |

## Engine/:

| File/Folder       | Description                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| `file_storage.py` | Contains the `FileStorage` class that serializes instances to a JSON file and deserializes JSON file to instances. |
| `__init__.py`     | Makes the folder a Python module.                                                                                  |
| `__pycache__/`    | This folder contains Python3 byte code files that are automatically generated by Python.                           |

## Tests/:

| File/Folder    | Description                                                            |
| -------------- | ---------------------------------------------------------------------- |
| `__init__.py`  | Makes the folder a Python module.                                      |
| `test_models/` | This folder contains all the unit tests for the models in the project. |

## Test/Test_Models/:

| File/Folder            | Description                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------------- |
| `__init__.py`          | Makes the folder a Python module.                                                        |
| `__pycache__/`         | This folder contains Python3 byte code files that are automatically generated by Python. |
| `test_base_model.py`   | Contains the unit tests for the `BaseModel` class.                                       |
| `test_engine/`         | This folder contains all the unit tests for the engine in the project.                   |
| `test_file_storage.py` | Contains the unit tests for the `FileStorage` class.                                     |

## Test/Test_Models/Test_Engine/:

| File/Folder            | Description                                          |
| ---------------------- | ---------------------------------------------------- |
| `__init__.py`          | Makes the folder a Python module.                    |
| `test_file_storage.py` | Contains the unit tests for the `FileStorage` class. |