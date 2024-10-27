"""Bottle game"""

def generate_bottles(round: int) -> list:
    """
    func recieve number of the round and generates grid by the round difficulty
    """
    bottles = [
            [[1, 2, 1, " "], [2, 1, 2, " "], [2, 1, " ", " "]],
            [[1, 2, 3, 2], [2, 1, 3, " "], [3, 2, " ", " "], [3, 1, 1, " "]],
            [[1, 2, 3, 2, " "], [2, 1, 3, 4, " "], [3, 2, 4, 3, " "], [3, 4, 1, 2," "], [4, 1, 4, 1, " "]],
            [[1, 5, 3, 5, " ", " "], [2, 5, 3, 4, 3, 1], [3, 5, 4, 3, 1, " "], [3, 4, 1, 2, " ", " "], [2, 5, 4, 1, 2, " "], [2, 1, 4, 2, 5, " "]],
            [[1, 2, 3, 2], [2, 1, 3, " "], [3, 2, " ", " "], [3, 1, 1, " "]]
            ]
    return bottles[round - 1]

def board_print(bottles: list, num: int = 3) -> tuple:
    """prints board"""
    counter = 1
    if num == 4:
        x = 3
    else:
        x = num - 1
    for j in range(x, -1, -1):
        for bottle in bottles:
            if counter == num:
                print(f"|{bottle[j]}| ")
                counter = 1
            else:
                counter += 1
                print(f"|{bottle[j]}| ", end="")

def check_for_victory(bottles: list) -> bool:
    """Check whether user won"""
    checkers = []
    for bottle in bottles:
        if all(i == bottle[0] for i in bottle):
            checkers.append(True)
        else:
            checkers.append(False)
    return all(checkers)

def get_user_input(num: int):
    """get input"""
    print("З котрої пляшки в котру бажаєте перемістити цифру?")
    change = input(">>> ").split()
    change_lst = [char for char in change]
    if len(change) > 2 or not all(i in " 1234567" for i in change_lst):
        return "\nДозволено вводити тільки одне переміщення за раз!\n Спробуйте ще раз!\n"
    if len(change) < 2:
        return "\nВи ввели занадто мало даних, попробуйте ще раз!\n"
    if change[0] == change[1]:
        return "\nДозволено вводити тільки різні номери комірок\n"
    change = [change[0], change[1]]
    if len(change) == 2 and change[0].isnumeric() and change[1].isnumeric() and \
0 < int(change[0]) <= num and 0 < int(change[1]) <= num:
        return [int(change[0]), int(change[1])]
    return "\nВи ввели дані некоректно\nВводьте дані за зразком - 1 2\n"

def main():
    """
    makes smth
    """
    print(" Привіт, давайте зіграймо в гру\n \
Ваше завдання - перемістити всі однакові цифри до однієї комірки.\n \
Щоб перемістити цифру з комірки X в комірку Y введіть X Y.\n \
Можна вводити лише одне переміщення за раз!\n \
Вдалої гри!")
    counter_of_failures = 0
    print("Оберіть складність для свого рівня (1-5)")
    round = input(">>> ")
    x = False
    while not x:
        try:
            round = int(round)
            if 1 <= round <= 5:
                x = True
        except TypeError:
            print(f"Рівня | {round} | не існує, введіть будь ласка значення від 1 до 5")
    possible_num = [3, 4, 5, 6, 7]
    num = possible_num[round-1]
    bottles = generate_bottles(round)
    print( " №1  №2  №3  №4")
    board_print(bottles, num)
    failure =True
    victory = False
    while not victory and failure:

        if counter_of_failures == 3:
            print("ПРОГРАШ\nВИ зробили занадто багато помилок")
            failure = False
            continue

        change = get_user_input(num)
        if isinstance(change, str):
            print(change)
            counter_of_failures += 1
            continue
        bottle_from, bottle_to = change[0]-1, change[1]-1

        for i, bottle in enumerate(bottles):

            if i == bottle_from: #перевіряємо чи це пляшка з якої нам треба перелити рідину
                if " " in bottle:
                    idx_1 = bottle.index(" ") - 1
                else:
                    idx_1 = num - 1
                new_item = bottle[idx_1]

                try:
                    idx = bottles[bottle_to].index(" ")
                    bottles[bottle_to][idx] = new_item
                    del bottles[i][idx_1]
                    bottles[i].append(" ")
                    board_print(bottles, num)
                except ValueError:
                    print(f"Пляшка номер {bottle_to + 1} вже повна")
                    counter_of_failures += 1
                victory = check_for_victory(bottles)
    if victory:
        print("\n\nВИ ПЕРЕМОГЛИ!\nВІТАЮ!")

if __name__ == '__main__':
    main()
