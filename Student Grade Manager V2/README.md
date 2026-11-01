
# Student Grade Manager V2

A simple CLI-based student grade management system built with Python.

This project allows users to manage student information and grades through a command-line interface. It also uses JSON to store data permanently, so information remains available even after the program is closed.

## Features

- **Show Students** – Display all student records.
- **Add Students** – Add new students with their NIM and grades.
- **Search Students** – Find students by name or NIM.
- **Calculate Average** – Calculate each student's average grade.
- **Show Highest Grade** – Find the highest individual grade.
- **Delete Student** – Remove student records.
- **JSON Persistence** – Automatically save and load student data.
- **Input Validation** – Validate names, NIMs, and grades.
- **Error Handling** – Handle missing or invalid JSON files.

## Technologies Used

- Python
- JSON
- File Handling
- Exception Handling
- Functions
- Lists and Dictionaries

## Project Structure

```text
Student Grade Manager V2/
├── main.py
├── students.json
└── README.md
```

## How to Run

1. Make sure Python is installed on your computer.
2. Clone or download this repository.
3. Open the project folder in your terminal.
4. Run the following command:

```bash
python main.py
```

## Data Storage

Student records are stored in `students.json`.

The program automatically loads existing data when started and saves changes whenever a student is added or deleted.

If the JSON file does not exist, the program initializes with default student records.

## Learning Objectives

This project was developed to practice:

- Python functions and modular programming.
- Working with lists and dictionaries.
- Input validation and exception handling.
- Reading and writing JSON files.
- Building interactive CLI applications.

## Version

**Version:** 2.0

**Status:** Completed
