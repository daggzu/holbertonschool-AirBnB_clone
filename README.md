# Holberton School - AirBnB Clone

## Table of Contents

- [Project Description](#project-description)
- [Learning Objectives](#learning-objectives)
- [Project Usage](#project-usage)
  - [Interactive Mode](#interactive-mode)
  - [Non-Interactive Mode](#non-interactive-mode)
- [Project Structure](#project-structure)
  - [Models/](#models)
  - [Engine/](#engine)
  - [Tests/](#tests)
  - [Test/Models/](#testmodels)
  - [Test/Engine/](#testengine)
- [How to Run the Tests](#how-to-run-the-tests)
- [Authors](#authors)
- [License](#license)

## Project Description

The AirBnB Console project provides a simple command interpreter for managing various objects related to AirBnB. It enables users to create, retrieve, update, and delete objects of different types, making it a useful tool for managing AirBnB-related data.

### Use Cases:

- Create new objects (e.g., User, Place).
- Retrieve an object from a file, database, etc.
- Perform operations on objects (e.g., count, compute statistics).
- Update attributes of an object.
- Destroy an object.

## Learning Objectives

This project encompasses various learning objectives, including:

- Creating a Python package for organizing modules.
- Building a command interpreter in Python using the `cmd` module.
- Implementing unit testing for a large project.
- Serializing and deserializing objects.
- Writing and reading JSON files.
- Managing `datetime` in Python.
- Working with UUIDs.
- Handling named arguments in functions.

## Project Usage

### Interactive Mode

To use the AirBnB Console in interactive mode, run the following command:

```bash
$ ./console.py

In the interactive mode, you can enter commands directly and receive responses in real-time.
Example Commands in Interactive Mode:

bash

(hbnb) help
(hbnb) create BaseModel
(hbnb) show BaseModel 1234-1234-1234
(hbnb) destroy BaseModel 1234-1234-1234
(hbnb) update BaseModel 1234-1234-1234 first_name "Bety"
(hbnb) all BaseModel
(hbnb) quit

Non-Interactive Mode

To use the AirBnB Console in non-interactive mode, you can pipe commands into the console as shown in the following examples:

bash

$ echo "create BaseModel" | ./console.py
$ echo "show BaseModel 1234-1234-1234" | ./console.py
$ echo "destroy BaseModel 1234-1234-1234" | ./console.py
$ echo "all BaseModel" | ./console.py

Project Structure

The project is organized as follows:

    models/ - Contains classes used in the project.
    engine/ - Contains the storage engine for the project.
    tests/ - Contains unit tests for the project.

Models/

    amenity.py - Contains the Amenity class.
    base_model.py - Contains the BaseModel class, the parent class for other classes.
    city.py - Contains the City class.
    place.py - Contains the Place class.
    review.py - Contains the Review class.
    state.py - Contains the State class.
    user.py - Contains the User class.

Engine/

    file_storage.py - Contains the FileStorage class for serializing and deserializing objects.

Tests/

    test_models/ - Contains unit tests for the models.
    test_engine/ - Contains unit tests for the engine.

Test/Models/

    test_base_model.py - Contains unit tests for the BaseModel class.
    test_engine/ - Contains unit tests for the engine.

Test/Engine/

    test_file_storage.py - Contains unit tests for the FileStorage class.

How to Run the Tests

To run the unit tests for the project, use the following command:

bash

$ python -m unittest discover tests

Authors

    Your Name
    Another Author

License

This project is licensed under the MIT License. See the LICENSE file for details.

rust


Make sure to replace `[Your Name](https://github.com/yourgithubusername)` and `[Another Author](https://github.com/anothergithubusername)` with the actual names and GitHub profiles of the authors.

This updated README provides a more structured and comprehensive overview of your project. You can u
