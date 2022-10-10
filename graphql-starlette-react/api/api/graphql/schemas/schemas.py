import time
import typing

import strawberry
from strawberry import Schema

from api.data import Books
from api.graphql.mutations import add_book
from api.graphql.types import Book


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=Books.get_books)


@strawberry.type
class Mutation:
    add_book = strawberry.mutation(resolver=add_book)


schema = Schema(query=Query, mutation=Mutation)
