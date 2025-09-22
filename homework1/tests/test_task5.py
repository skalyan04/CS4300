import pathlib
import sys
import subprocess

# Add src/ to path for imports
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "src"))
import task5


def test_favorite_books_length():
    # Ensure the list has at least 5 books
    assert len(task5.favorite_books) >= 5


def test_favorite_books_slicing():
    # First three books
    first_three = task5.favorite_books[:3]
    assert len(first_three) == 3
    assert first_three[0][0] == "The Hobbit"   # title of first book
    assert first_three[1][0] == "Dracula"      # title of second book
    assert first_three[1][1] == "Bram Stoker"  # author of second book


def test_student_database_contents():
    db = task5.student_db
    assert "James" in db
    assert db["James"] == "S123"
    assert db.get("Natasha") == "S789"


def test_task5_console_output():
    script_path = pathlib.Path(__file__).parent.parent / "src" / "task5.py"
    result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
    output = result.stdout.strip().splitlines()

    # Verify console output for books
    assert "First three books:" in output[0]
    assert "- The Hobbit by J.R.R. Tolkien" in output[1]
    assert "- Dracula by Bram Stoker" in output[2]
    assert "- Pride and Prejudice by Jane Austen" in output[3]

    # Verify student database output (skip blank line if present)
    assert "Student database:" in output[4] or "Student database:" in output[5]
    assert any("James: S123" in line for line in output)
    assert any("Steve: S456" in line for line in output)
    assert any("Natasha: S789" in line for line in output)
