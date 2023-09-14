from collections import namedtuple

Pair = namedtuple('Pair', ['first', 'second'])

def pair(x):
    def fn(y):
        return Pair(x, y)
    return fn

print(pair(10)(20))

def head(pair):
    return pair.first

def tail(pair):
    return pair.second

def range(left):
    def fn(right):
        if left > right:
            return None
        return Pair(left, range(left + 1)(right))
    return fn


xs = range(1)(5)
print(f"{xs=}")

def list_to_array(xs):
    rv = []
    while xs is not None:
        item = head(xs)
        rv.append(item)
        xs = tail(xs)
    return rv

def array_to_list(array):
    rv = None
    array.reverse()
    for e in array:
        rv = pair(e)(rv)

    return rv


def mmap(func):
    def inner(xs):
        if xs is None:
            return None
        return Pair(func(head(xs)), mmap(func)( tail(xs) ))
    return inner

print(f"{list_to_array(xs)=}")
print(f"{array_to_list(list_to_array(xs))=}")

print(f"{list_to_array(mmap(lambda x: x*x) (xs))=}")


fxs = range(1)(100)

def fizzBuzz(x):
    if x % 15 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    return x

print(f"{list_to_array(mmap(fizzBuzz) (fxs))=}")


def inf_curry(*args):
    items = []
    assert len(args) <= 1, "Expected a single argument to be passed"
    if len(args) == 0:
        return items

    def inner(arg=None):
        nonlocal items
        if arg is None:
            return items

        items.append(arg)
        return inner

    return inner(*args)


print(f"{inf_curry()=}")
print(f"{inf_curry(1)()=}")
print(f"{inf_curry(1)(2)(3)(4)(5)()=}")


"""
Pair(first=10, second=20)

xs=Pair(first=1, second=Pair(first=2, second=Pair(first=3, second=Pair(first=4,
second=Pair(first=5, second=None)))))

list_to_array(xs)=[1, 2, 3, 4, 5]

array_to_list(list_to_array(xs))=Pair(first=1, second=Pair(first=2,
second=Pair(first=3, second=Pair(first=4, second=Pair(first=5, second=None)))))

list_to_array(mmap(lambda x: x*x) (xs))=[1, 4, 9, 16, 25]

list_to_array(mmap(fizzBuzz) (fxs))=[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz',
'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz', 31, 32, 'Fizz',
34, 'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'Fizz', 43, 44, 'FizzBuzz', 46,
47, 'Fizz', 49, 'Buzz', 'Fizz', 52, 53, 'Fizz', 'Buzz', 56, 'Fizz', 58, 59,
'FizzBuzz', 61, 62, 'Fizz', 64, 'Buzz', 'Fizz', 67, 68, 'Fizz', 'Buzz', 71,
'Fizz', 73, 74, 'FizzBuzz', 76, 77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 83, 'Fizz',
'Buzz', 86, 'Fizz', 88, 89, 'FizzBuzz', 91, 92, 'Fizz', 94, 'Buzz', 'Fizz', 97,
98, 'Fizz', 'Buzz']

inf_curry()=[]
inf_curry(1)()=[1]
inf_curry(1)(2)(3)(4)(5)()=[1, 2, 3, 4, 5]
"""
