# task5.py

# List of favorite books (title, author)
favorite_books = [
    ("The Hobbit", "J.R.R. Tolkien"),
    ("Dracula", "Bram Stoker"),
    ("Pride and Prejudice", "Jane Austen"),
    ("Carmilla", "Sheridan Le Fanu"),
    ("Salem's Lot", "Stephen King"),
]

# Print the first three books using slicing
print("First three books:")
for book in favorite_books[:3]:
    print(f"- {book[0]} by {book[1]}")

# Dictionary: student database
student_db = {
    "James": "S123",
    "Steve": "S456",
    "Natasha": "S789",
}

# Print student database
print("\nStudent database:")
for name, sid in student_db.items():
    print(f"{name}: {sid}")
