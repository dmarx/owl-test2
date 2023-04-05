"""
The following is a concise implementation of FizzBuzz written in Python 3.

Usage:
    - Call `fizzbuzz()` with an integer argument `n` to print numbers from 1 to `n`, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both 3 and 5 with "FizzBuzz".

Example:
    - fizzbuzz(15) would output the following:
        1
        2
        Fizz
        4
        Buzz
        Fizz
        7
        8
        Fizz
        Buzz
        11
        Fizz
        13
        14
        FizzBuzz
"""


def fizzbuzz(n: int) -> None:
    """
    Prints numbers from 1 to n, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz",
    and multiples of both 3 and 5 with "FizzBuzz".
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
"""
