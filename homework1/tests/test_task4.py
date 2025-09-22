# test_task4.py

import pathlib
import sys
import subprocess

# Add src/ to path for imports
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "src"))
import task4


def test_discount_with_integers():
    assert task4.calculate_discount(100, 20) == 80
    assert task4.calculate_discount(250, 50) == 125


def test_discount_with_floats():
    result = task4.calculate_discount(99.99, 15.5)
    assert round(result, 2) == 84.49  # rounding for float precision


def test_invalid_discount():
    try:
        task4.calculate_discount(100, -10)
    except ValueError as e:
        assert str(e) == "Discount must be between 0 and 100"

    try:
        task4.calculate_discount(100, 150)
    except ValueError as e:
        assert str(e) == "Discount must be between 0 and 100"


# Optional: console output test
def test_task4_console_output():
    script_path = pathlib.Path(__file__).parent.parent / "src" / "task4.py"
    result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
    output = result.stdout.strip().splitlines()

    assert "Final price (int): 80" in output
    assert "Final price (float):" in output[1]
    assert "84.49" in output[1]
