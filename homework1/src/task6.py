# task6.py
import pathlib

def count_words(file_path):
    """Counts the number of words in a text file."""
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        words = text.split()  # split by whitespace
        return len(words)


if __name__ == "__main__":
    # Path to the text file
    file_path = pathlib.Path(("/home/student/cs4300/homework1/task6_read_me.txt"))
    total_words = count_words(file_path)
