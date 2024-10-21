"""HW"""
from copy import deepcopy
def happy_number(number: int) -> bool:
    """
    Determines if a ticket number is a happy number.

    Parameters:
    num (int): The ticket number to check.

    Returns:
    bool: True if the ticket is a happy number, False otherwise.

    >>> happy_number(1234)
    False
    >>> happy_number(32100123)
    True
    >>> happy_number(159123)
    True
    """
    str_number = f'{str(number):0>8}'
    str_number = [num for num in str_number]
    
    first_half, second_half = str_number[:4], str_number[4:]
    first = sum([int(i) for i in first_half])
    second = sum([int(i) for i in second_half])

    while first > 9:
        first = sum([int(i) for i in str(first)])
    while second > 9:
        second = sum([int(i) for i in str(second)])

    return second == first


def count_happy_numbers(n: int) -> int:
    """
    Counts the number of happy tickets from 1 to n inclusive.

    Parameters:
    n (int): The upper limit of ticket numbers to check.

    Returns:
    int: The count of happy tickets in the range.

    >>> count_happy_numbers(10001)
    1
    >>> count_happy_numbers(10010)
    2
    >>> count_happy_numbers(10100)
    12
    >>> count_happy_numbers(100000)
    9999
    """
    counter = 0
    for i in range(1, n+1):
        if happy_number(i):
            counter += 1
    return counter

def happy_numbers(m: int, n: int) -> list[int]:
    """
    Generates a list of happy ticket numbers within the given range.

    Parameters:
    m (int): The lower limit of ticket numbers (inclusive).
    n (int): The upper limit of ticket numbers (inclusive).

    Returns:
    list[int]: A list of happy ticket numbers in the range.

    >>> happy_numbers(1, 10001)
    [10001]
    >>> happy_numbers(10001, 10010)
    [10001, 10010]
    >>> happy_numbers(1, 11)
    []
    >>> happy_numbers(10001, 10100)
    [10001, 10010, 10019, 10028, 10037, 10046, 10055, 10064, 10073, 10082, 10091, 10100]
    """
    numbers = []
    for i in range(m, n+1):
        if happy_number(i):
            numbers.append(i)
    return numbers

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
