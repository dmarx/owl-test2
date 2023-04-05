The following is a concise implementation of fizzbuzz.

```python
def fizzbuzz(n: int) -> List[Union[int, str]]:
    """
    Returns a list of numbers from 1 to n, with the following replacements:
    - Multiples of 3 are replaced with 'Fizz'
    - Multiples of 5 are replaced with 'Buzz'
    - Multiples of both 3 and 5 are replaced with 'FizzBuzz'
    """
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(i)
    return result
```
