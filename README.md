## Prerequisites
Before running the tests, ensure you have the following prerequisites:

- Python 3.11 or higher installed
- Poetry for managing dependencies
- Web browsers (Chrome and/or Firefox) installed for running tests local

## Setup 
1. Clone repo to your local machine.
2. Open the project in your favorite code editor.
3. Perform ```poetry install```.
4. Perform ```poetry shell```.


## Run test:

To run the tests, execute the following command in your project directory:
```poetry run pytest tests/test_create_task.py```

To generate an HTML test report, you can use the following command:
```poetry run pytest tests/test_create_task.py -v -s --html=./test_reports/create_task.html --self-contained-html --capture sys -rP -rF```

- ```-v```: Enables verbose output, providing detailed information about the tests being executed.

- ```-s```: Allows pytest to display standard output (print statements) from your tests in the terminal.

- ```--html=./test_reports/debugbear.html```: This option tells pytest to generate an HTML test report and save it as debugbear.html in the test_reports directory. You can customize the filename and directory as needed.

- ```--self-contained-html```: Ensures that the HTML report is self-contained, meaning it includes all necessary resources (e.g., stylesheets and JavaScript) within the report itself.

- ```--capture sys```: Captures standard output and standard error for each test and displays it in the test report.

- ```-rP -rF```: These options control the display of test summary information. -rP displays the passed tests first, and -rF shows the failed tests first. You can adjust these options based on your preference.