# test_task2.py

import pathlib
import sys
import subprocess

# Import functions directly for unit testing
# More fluid way of importing instead of specific file paths
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "src"))
import task2


def test_integer():
    assert isinstance(task2.get_integer(), int)
    assert task2.get_integer() == 42


def test_float():
    assert isinstance(task2.get_float(), float)
    assert task2.get_float() == 3.14


def test_string():
    assert isinstance(task2.get_string(), str)
    assert task2.get_string() == "Hello, Python"


def test_boolean():
    assert isinstance(task2.get_boolean(), bool)
    assert task2.get_boolean() is True


# Optional: test console output with subprocess (like Task 1)
def test_task2_console_output():
    script_path = pathlib.Path(__file__).parent.parent / "src" / "task2.py"
    result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
    output = result.stdout.strip().splitlines()

    assert "Integer: 42" in output
    assert "Float: 3.14" in output
    assert "String: Hello, Python" in output
    assert "Boolean: True" in output
