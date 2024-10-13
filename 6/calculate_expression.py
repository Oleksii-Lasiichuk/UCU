"""calculating expression in str"""
def calculate_expression(expression):
    """
    function calculates expression from string

    >>> calculate_expression("Скільки буде 5 помножити на 5 помножити на 7 додати 2?")
    177
    >>> calculate_expression("Скільки буде 6 помножити на 5 відняти 7 помножити на 2?")
    46
    >>> calculate_expression("Скільки буде 6 помножити на 5 мінус 7 помножити на 2?")
    46
    >>> calculate_expression("Скільки буде 5 плюс 5?")
    10
    >>> calculate_expression("Скільки буде 2 помножити на 10 додати 7?")
    27
    >>> calculate_expression("Скільки буде 2 додати 10 помножити на 7?")
    84
    >>> calculate_expression("Скільки буде 2?")
    2
    >>> calculate_expression('Скільки буде 10 поділити на -2 додати 11 мінус -3?')
    9
    >>> calculate_expression("Скільки буде -5 помножити на 5 додати 7?")
    -18
    >>> calculate_expression('')
    'Неправильний вираз!'
    """
    try:
        list_expression = expression.split()
        if list_expression[0] != "Скільки" and list_expression[1] != "буде" \
            or list_expression[-1].count("?") == 0:
            return 'Неправильний вираз!'

        del list_expression[:2]

        #finding and deliting question mark
        list_expression[-1] = list_expression[-1].replace("?", "" )

        #changing "помножити на" -> "помножити"
        for i, el in enumerate(list_expression):
            if el == "помножити":
                del list_expression[i+1]
            elif el == "поділити":
                del list_expression[i+1]

        lenght = len(list_expression)

        if lenght % 2 == 0:
            return "Неправильний вираз!"

        if lenght == 1 and list_expression[0].isdigit():
            return int(list_expression[0])

        #checking for correct input
        for i in range(lenght):
            if i % 2 == 0:
                list_expression[i] = int(list_expression[i])
            else:
                if not list_expression[i] in ("помножити", "поділити",
                                                "додати", "мінус",
                                                "плюс", "відняти"
                                            ):
                    return "Неправильний вираз!"

        # calculating
        current_num = int(list_expression[0])
        for i in range(1, lenght, 2):
            if list_expression[i] == "помножити":
                current_num *= int(list_expression[i+1])
            elif list_expression[i] == "поділити":
                current_num /= int(list_expression[i+1])
            elif list_expression[i] in ("додати", "плюс"):
                current_num += int(list_expression[i+1])
            elif list_expression[i] in ("мінус", "відняти"):
                current_num -= int(list_expression[i+1])
        return int(current_num)

    except (TypeError, ValueError, ZeroDivisionError, IndexError):
        return "Неправильний вираз!"

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
