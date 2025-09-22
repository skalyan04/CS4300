# test_task6.py
import pathlib
import sys
import subprocess

# Add src/ to path for imports
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "src"))
import task6


def test_count_words_function():
    file_path = pathlib.Path("/home/student/cs4300/homework1/task6_read_me.txt")
    count = task6.count_words(file_path)
    
    # Based on the way that it copy pasted, there are 163 words (adjust if needed)
    assert count == 163


def test_task6_console_output():
    file_path = pathlib.Path("/home/student/cs4300/homework1/src/task6.py")
    result = subprocess.run([sys.executable, str(file_path)], capture_output=True, text=True)
    output = result.stdout.strip()
    
    # Check that the output mentions total words
    assert "Total words in task6_read_me.txt:" in output
    assert "163" in output  # match the correct word count
