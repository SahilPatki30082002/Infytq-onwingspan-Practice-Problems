class Book:
    def __init__(self, title, author): self.title = title; self.author = author
    def get_title(self): return f"Title: {self.title}"
    def get_author(self): return f"Author: {self.author}"
PP = Book("Pride and Prejudice", "Jane Austen"); H = Book("Harry Potter", "J.K. Rowling"); WP = Book("War and Peace", "Leo Tolstey");print(PP.get_title());print(PP.get_author())