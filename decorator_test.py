import random
import time
import timeit
import functools

def bench(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        t0 = time.perf_counter()
        ret = func(*args, **kwargs)
        t1 = time.perf_counter()
        print(f"[{func.__name__}] Took Time : {t1-t0}")
        return t1-t0
    return inner


def fn(x: int) -> int:
    count:int = 0
    for _ in range(x):
        count += 1
    return count


def cache(func):
    cached = {}
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return cached[args]
        except KeyError as ke:
            cached[args] = func(*args, **kwargs)
            return cached[args]
    return inner


@cache
def fn_cached(x: int) -> int:
    count:int = 0
    for _ in range(x):
        count += 1
    return count

l_b, h_b = int(1e6)-5, int(1e6)

@bench
def test(n: int):
    for _ in  range(n):
        n = random.randint(l_b, h_b)
        got = fn(n)
        assert(got == n)


@bench
def test_cached(n : int):
    for _ in  range(n):
        n = random.randint(l_b, h_b)
        got = fn_cached(n)
        assert(got == n)


def main() -> None:
    n = int(1e3)
    n = eval(input("Enter n: "))
    test(n)
    test_cached(n)

if __name__ == "__main__":
    exit(main())



"""
python3 -i decorator_test.py
>>> test(1000)
[test] Took Time : 39.68231679999735
39.68231679999735
>>> test_cached(1000)
[test_cached] Took Time : 0.0014149999478831887
0.0014149999478831887
"""
