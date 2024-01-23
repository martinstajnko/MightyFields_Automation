""" Pytest configuration file."""

import pytest

def pytest_addoption(parser):
    """
    Add command-line options to control the test.

    Args:
        parser: The pytest command line parser.
    """
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser: chrome or firefox"
    )
    parser.addoption(
        "--headless", action="store", default=False, help="headless: true or false"
    )
    parser.addoption(
        "--full_screen", action="store", default=False, help="full_screen: true or false"
    )


@pytest.fixture
def command_line_arguments(request) -> dict:
    """
    Fixture to retrieve command-line arguments.

    Args:
        request: The pytest request object.

    Returns:
        dict: Containing the command-line arguments.
    """
    return {
        "browser": request.config.getoption("--browser"),
        "headless": request.config.getoption("--headless"),
        "full_screen": request.config.getoption("--full_screen"),
    }