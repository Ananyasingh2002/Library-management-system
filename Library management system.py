#Library management system
import tkinter as tk
from tkinter import messagebox

class Library:

    def __init__(self, book, author):
        self._book = book
        self._author = author

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, new_book):
        if new_book is not None:
            self._book = new_book
        else:
            print("Book name can't be Empty.")
       
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if new_author is not None:
            self._author = new_author
        else:
            print("Author name can't be Empty.")

    @property
    def about(self):
        return f"The name of the book: {self._book}\n The author of the book: {self._author}"


def add_detail():
    book = book_entry.get()
    author = author_entry.get()
    return Library(book, author)


def view_library(library):
    if not library:
        messagebox.showinfo("Library", "The list is empty")
    else:
        books_info = ""
        for index, book in enumerate(library, start=1):
            books_info += f"{index}. The name of the Book: {book.book}\n    The author of the book: {book.author}\n\n"
        messagebox.showinfo("Current Books", books_info)

def add_book():
    book = book_entry.get().strip()
    author = author_entry.get().strip()

    if book and author:
        book_list.append(Library(book, author))
        book_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)
        messagebox.showinfo("Library", "Book added successfully!")
    else:
        messagebox.showerror("Error", "Both Book name and Author name must be filled!")


def delete_book():
    index = delete_entry.get().strip()
    if index.isdigit() and 1 <= int(index) <= len(book_list):
        del book_list[int(index) - 1]
        view_library(book_list)
        delete_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Invalid index!")


def exit_library():
    root.destroy()


book_list = []

root = tk.Tk()
root.title("Library Management System")

# Set the background color and padding
root.configure(bg="#f0f0f0")
root.geometry("400x400")

# Create a custom font
custom_font = ("Arial", 12)

# Create labels and entry fields
book_label = tk.Label(root, text="Book Name:", font=custom_font, bg="#f0f0f0")
book_label.pack(pady=10)

book_entry = tk.Entry(root, font=custom_font)
book_entry.pack(pady=5)

author_label = tk.Label(root, text="Author Name:", font=custom_font, bg="#f0f0f0")
author_label.pack(pady=10)

author_entry = tk.Entry(root, font=custom_font)
author_entry.pack(pady=5)

# Create buttons with colors and padding
add_button = tk.Button(root, text="Add Book", font=custom_font, bg="#4CAF50", fg="white", command=add_book)
add_button.pack(pady=10)

view_button = tk.Button(root, text="View Library", font=custom_font, bg="#008CBA", fg="white",
                        command=lambda: view_library(book_list))
view_button.pack(pady=5)

delete_label = tk.Label(root, text="Enter index to delete:", font=custom_font, bg="#f0f0f0")
delete_label.pack(pady=10)

delete_entry = tk.Entry(root, font=custom_font)
delete_entry.pack(pady=5)

delete_button = tk.Button(root, text="Delete Book", font=custom_font, bg="#f44336", fg="white", command=delete_book)
delete_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", font=custom_font, bg="#555", fg="white", command=exit_library)
exit_button.pack(pady=10)

root.mainloop()
