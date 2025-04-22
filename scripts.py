"""Utility scripts for development workflows.

This module is a temporary workaround until Poetry supports scripts natively.
See: https://github.com/sdispater/poetry/issues/241

These scripts can be run through Poetry using `poetry run <command>`.
"""
from subprocess import check_call


def style() -> None:
    """Check code formatting using Black.
    
    Runs Black in check mode with diff output to show what formatting changes 
    would be made without actually changing any files.
    """
    check_call(
        ["black", "--check", "--diff", "src/"],
    )


def restyle() -> None:
    """Apply code formatting using Black.
    
    Automatically reformats all Python code in the src/ directory to comply with 
    Black's style guide.
    """
    check_call(["black", "src/"])


def lint() -> None:
    """Run static code analysis using Pylint.
    
    Checks the codebase for errors, bad practices, and style issues according to
    the project's Pylint configuration.
    """
    check_call(["pylint", "src/"])


def test() -> None:
    """Run the test suite using pytest.
    
    Executes all unit tests in the project to verify that everything is working
    correctly.
    """
    check_call(["pytest"])
