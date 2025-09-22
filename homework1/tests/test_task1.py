# test_task1.py

import subprocess
import sys
import pathlib

def test_task1_output():
    # Absolute path to task1.py
    script_path = pathlib.Path("/home/student/cs4300/homework1/src/task1.py")

    result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
    output = result.stdout.strip()

    assert output == "Hello, World!"
