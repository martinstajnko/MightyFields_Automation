## Prerequisites
Before running the tests, ensure you have the following prerequisites:

- Python 3.11 or higher installed
- Poetry for managing dependencies
- Web browsers (Chrome and/or Firefox) installed for running tests

## Setup 
1. Clone repo to your local machine.
2. Open the project.
3. Perform ```poetry install```.
4. Perform ```poetry shell```.


## Run test:

To run the tests, execute the following command in your project directory:
```poetry run pytest tests/test_create_task.py```

To generate an HTML test report, you can use the following command:
```poetry run pytest tests/test_create_task.py -v -s --html=./test_reports/create_task.html --self-contained-html --capture sys -rP -rF```

- ```-v```: Enables verbose output, providing detailed information about the tests being executed.

- ```-s```: Allows pytest to display standard output (print statements) from your tests in the terminal.
