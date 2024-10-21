"""HW lucky number"""
def sieve_flavius(n: int) -> list[int]:
    """Generates a list of lucky numbers not exceeding the given number n.

    Parameters:
    n (int): The upper limit for generating lucky numbers.

    Returns:
    list[int]: A list of lucky numbers up to n.

    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    >>> sieve_flavius(33)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    >>> sieve_flavius(0)
    []
    """
    numbers = [i for i in range(1, n+1) if i%2 == 1]
    dividing_num = 3
    counter = 0
    
    counter = 1
    while counter < len(numbers):
        dividing_num = numbers[counter]
        numbers = [num for i, num in enumerate(numbers) if (i + 1) % dividing_num != 0]
        counter += 1
    return numbers

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())