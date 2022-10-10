from api.graphql.types import Book


class Books:
    books = [
        Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
        ),
        Book(
            title="Harry Potter",
            author="J.K Rowling",
        ),
    ]

    @classmethod
    def get_books(cls):
        return cls.books

    @classmethod
    def add_books(cls, book: Book):
        cls.books.append(book)
