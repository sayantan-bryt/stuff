import time

from api.data import Books
from api.graphql.types import Book


async def add_book(self, title: str, author: str) -> Book:
    print(f"Adding {title=} by {author=}")
    time.sleep(0.2)
    book = Book(title=title, author=author)
    Books.add_books(book)
    return book
