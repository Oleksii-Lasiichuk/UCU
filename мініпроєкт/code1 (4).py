"""BAD CODE"""


def check_circle_inscribed_square0(r, a):
    r, a = int(r), int(a)
    if r == int(a / 2):
        return True
    return False


"""OUR CODE"""


def check_circle_inscribed_square(r: int | float, a: int | float) -> bool:
    """
    Check if the circle is inscribed

    :param r: int or float, The radius of the circle.
    :param a: int or float, The length of the square side.
    :return: bool, True if circle is inscribed, otherwise False.
    """
    return r == a / 2


# changes:
# 1. get rid of all int() func because it rounds all the numbers down
# 2. unnecessary return statements


"""CHAT GPT"""


def check_circle_inscribed_square2(r, a):
    # Перевірка, чи діаметр кола дорівнює стороні квадрата
    if 2 * r == a:
        return True
    return False


"""У поточному коді є кілька моментів, які призводять до помилок:
Умова перевірки: У коді перевіряється, чи радіус 
r дорівнює половині сторони квадрата a. 
Однак вписане коло має діаметр, що дорівнює стороні квадрата, 
тобто правильна умова має перевіряти, чи діаметр 
2×r дорівнює a, а не просто радіус r.

Необхідність перетворення типів: Код перетворює 
r та a в цілі числа, що може призвести до втрати точності.
Перетворення слід застосовувати лише для перевірки рівності,
щоб уникнути помилок з округленням."""
