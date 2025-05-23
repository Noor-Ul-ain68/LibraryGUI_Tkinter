# Library Management System GUI

This project is a GUI-based Library Management System built with Python Tkinter.

## Features

- Add Books and eBooks with details (title, author, ISBN, download size for eBooks)  
- Lend books and return them  
- Remove books from the library  
- View books by author  
- Automatically disable download size input unless eBook checkbox is selected  

## How to Run

1. Clone or download the repository  
2. Create and activate a Python virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
---

## 🧠 PyQt GUI Version

This version uses PyQt5 to create a desktop GUI for the same library system.

### 📂 File:
- `pyqt_app.py`

### 🧪 Features:
- Add books (title, author, ISBN)
- View all added books in a list
- Backend logic shared with Tkinter version

### 💡 How to Run (with PyQt environment)

1. Activate the virtual environment:
   ```bash
   venv_pyqt\Scripts\activate
