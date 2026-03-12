"""..."""

from functools import lru_cache

@lru_cache(maxsize=4)
def fib(n):
    """fibon"""

    if n < 2:
        return n
    return fib(n- 1) + fib(n- 2)

print(fib(400))

@lru_cache(maxsize=3)
def fib1(n):
    """fibon"""

    if n < 2:
        return n
    return fib1(n - 2) + fib1(n - 1)

print(fib1(400))
