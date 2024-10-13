'''big digits'''

import sys

ZERO = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]

ONE = [" * ",
       "** ",
       " * ",
       " * ",
       " * ",
       " * ",
       "***"]

TWO = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
THREE = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
FOUR = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
FIVE = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
SIX = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
SEVEN = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
EIGHT = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
NINE = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

DIGITS = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]


def return_digits(number: str) -> str:
    '''
    function desplay digits
    
    >>> return_digits('4128')
    '   4   1  222  888 \\n  44  11 2   28   8\\n 4 4   1 2  2 8\
   8\\n4  4   1   2   888 \\n444444 1  2   8   8\\n   4   1 2    8   8\\n   4\
  11122222 888 '

    >>> return_digits('0987654321')
    '  000   9999 888 77777 666 55555   4   333  222  1 \\n\
 0   0 9   98   8    76    5      44  3   32   211 \\n\
0     09   98   8   7 6    5     4 4      32  2  1 \\n\
0     0 9999 888   7  6666  555 4  4    33   2   1 \\n\
0     0    98   8 7   6   6    5444444    3 2    1 \\n\
 0   0     98   87    6   65   5   4  3   32     1 \\n\
  000      9 888 7     666  555    4   333 22222111'
    '''
    final_result = []
    for i in range(7):
        result = ''
        for el in number:
            num = int(el)
            element = DIGITS[num][i]
            element = element.replace("*", el)
            result += element
        final_result.append(result)

    return "\n".join(final_result)

try:
    digits = sys.argv[1]
    print(return_digits(digits))
except IndexError:
    print("usage example: python bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
