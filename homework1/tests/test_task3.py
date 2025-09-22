# test_task3.py

import pathlib
import sys
import subprocess

# Add src/ to path for imports
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "src"))
import task3


def test_check_number():
    assert task3.check_number(5) == "Positive"
    assert task3.check_number(-3) == "Negative"
    assert task3.check_number(0) == "Zero"


def test_get_first_primes():
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert task3.get_first_primes(10) == expected_primes


def test_sum_1_to_100():
    assert task3.sum_1_to_100() == 5050


# Optional: console output check
def test_task3_console_output():
    script_path = pathlib.Path(__file__).parent.parent / "src" / "task3.py"
    result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
    output = result.stdout.strip().splitlines()

    assert "Check number -5: Negative" in output
    assert "Check number 0: Zero" in output
    assert "Check number 7: Positive" in output
    assert "First 10 primes: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]" in output
    assert "Sum 1 to 100: 5050" in output
