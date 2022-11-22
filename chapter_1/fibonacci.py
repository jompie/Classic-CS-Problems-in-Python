# recursive solution
def fib1(n: int) -> int:
    return n if n < 2 else fib1(n - 1) + fib1(n - 2)


# recursive with memoization
from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}


def fib2(n: int) -> int:
    if n not in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2)
    return memo[n]


# automatic memoization
from functools import lru_cache


@lru_cache(maxsize=None)
def fib3(n: int) -> int:
    return n if n < 2 else fib3(n - 1) + fib3(n - 2)


# itirative solution
def fib4(n: int) -> int:
    if n == 0:
        return n
    a: int = 0
    b: int = 1
    for _ in range(1, n):
        a, b = b, a + b
    return b


# fibonacci generator
from typing import Generator


def fib5(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    a: int = 0
    b: int = 1
    for _ in range(1, n):
        a, b = b, b + a
        yield b
