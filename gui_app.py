import tkinter as tk
from tkinter import messagebox, simpledialog
from book_library import Book, EBook, Library, BookNotAvailableError

# Create main window
root = tk.Tk()
root.title("Library Management System")
root.geometry("600x600")

# Create a Library object
library = Library()

# =================== eBook Checkbox Toggle Function ===================

def toggle_size_entry():
    if ebook_var.get():
        size_entry.config(state="normal")
    else:
        size_entry.delete(0, tk.END)
        size_entry.config(state="disabled")

# =================== Add Book Function ===================

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    isbn = isbn_entry.get()
    is_ebook = ebook_var.get()
    size = size_entry.get()

    if not title or not author or not isbn:
        messagebox.showerror("Error", "Title, Author, and ISBN are required.")
        return

    if is_ebook and not size:
        messagebox.showerror("Error", "Download size required for eBooks.")
        return

    if is_ebook:
        book = EBook(title, author, isbn, size)
    else:
        book = Book(title, author, isbn)

    library.add_book(book)
    messagebox.showinfo("Success", f"Book '{title}' added to the library.")
    update_book_list()

# =================== Other Functionalities ===================

def lend_book():
    isbn = simpledialog.askstring("Lend Book", "Enter ISBN of the book to lend:")
    if isbn:
        try:
            library.lend_book(isbn)
            messagebox.showinfo("Success", "Book lent successfully.")
            update_book_list()
        except BookNotAvailableError as e:
            messagebox.showerror("Error", str(e))

def return_book():
    isbn = simpledialog.askstring("Return Book", "Enter ISBN of the book to return:")
    if isbn:
        try:
            library.return_book(isbn)
            messagebox.showinfo("Success", "Book returned successfully.")
            update_book_list()
        except BookNotAvailableError as e:
            messagebox.showerror("Error", str(e))

def remove_book():
    isbn = simpledialog.askstring("Remove Book", "Enter ISBN of the book to remove:")
    if isbn:
        library.remove_book(isbn)
        messagebox.showinfo("Success", "Book removed from library.")
        update_book_list()

def view_books_by_author():
    author = simpledialog.askstring("Search by Author", "Enter author's name:")
    if author:
        books = list(library.books_by_author(author))
        if books:
            listbox.delete(0, tk.END)
            listbox.insert(tk.END, f"Books by {author}:")
            for book in books:
                listbox.insert(tk.END, str(book))
        else:
            messagebox.showinfo("Not Found", "No books by this author.")

def update_book_list():
    listbox.delete(0, tk.END)
    listbox.insert(tk.END, "Available Books:")
    for book in library:
        listbox.insert(tk.END, str(book))

# =================== GUI Layout ===================

# Labels & Entry Fields
tk.Label(root, text="Title:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Author:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
author_entry = tk.Entry(root)
author_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="ISBN:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
isbn_entry = tk.Entry(root)
isbn_entry.grid(row=2, column=1, padx=10, pady=5)

# eBook checkbox
ebook_var = tk.BooleanVar()
tk.Checkbutton(root, text="Is eBook?", variable=ebook_var, command=toggle_size_entry).grid(row=3, column=0, sticky="w", padx=10)

# eBook size field (initially disabled)
tk.Label(root, text="Download Size (MB):").grid(row=4, column=0, sticky="w", padx=10, pady=5)
size_entry = tk.Entry(root, state="disabled")
size_entry.grid(row=4, column=1, padx=10, pady=5)

# Button Frame
button_frame = tk.Frame(root)
button_frame.grid(row=5, column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="Add Book", command=add_book).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Lend Book", command=lend_book).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Return Book", command=return_book).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Remove Book", command=remove_book).grid(row=0, column=3, padx=5)
tk.Button(button_frame, text="View Books by Author", command=view_books_by_author).grid(row=0, column=4, padx=5)

# Book List Display
tk.Label(root, text="Library Inventory:").grid(row=6, column=0, columnspan=2, pady=(20, 0))
listbox = tk.Listbox(root, width=70)
listbox.grid(row=7, column=0, columnspan=2, pady=10)

update_book_list()

# Start GUI
root.mainloop()
