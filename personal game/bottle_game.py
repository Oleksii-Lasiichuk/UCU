"""Box game"""

def generate_boxes(round: int) -> list:
    """
    Function receives the round number and generates the grid based on round difficulty
    """
    boxes = [
            [[1, 2, 1, " "], [2, 1, 2, " "], [2, 1, " ", " "]],
            [[1, 2, 3, 2], [2, 1, 3, " "], [3, 2, " ", " "], [3, 1, 1, " "]],
            [[1, 2, 3, 2, " "], [2, 1, 3, 4, " "], [3, 2, 4, 3, " "], [3, 4, 1, 2," "], [4, 1, 4, 1, " "]],
            [[1, 5, 3, 5, 4, " "], [2, 5, 3, 4, 3, 1], [3, 5, 4, 3, 1, " "], [3, 4, 1, 2, " ", " "], [2, 5, 4, 1, 2, " "], [2, 1, 4, 2, 5, " "]],
            [[6, 5, 3, 5, 6, 1, 4], [2, 5, 3, 4, 3, 1, " "], [6, 5, 4, 3, 1, 3, " "], [3, 4, 1, 2, 6, " ", " "], [2, 6, 4, 1, 2, 5, " "], [2, 6, 4, 2, 5, 1, " "], [2, 6, 4, 5, 1, 3, " "]],
            ]
    return boxes[round - 1]

def board_print(boxes: list, hp: int, num: int) -> tuple:
    """prints board"""
    print(f"Your HP is {hp}/3")
    for i in range(1, num+1):
        print(f" №{str(i)} ", end = '')
    print()
    counter = 1

    x = 3 if num == 3 else num - 1

    for j in range(x, -1, -1):
        for box in boxes:
            if counter == num:
                print(f"|{box[j]}| ")
                counter = 1
            else:
                counter += 1
                print(f"|{box[j]}| ", end="")

def check_for_victory(boxes: list) -> bool:
    """Check whether user won"""
    checkers = []
    for box in boxes:
        if all(i == box[0] for i in box):
            checkers.append(True)
        else:
            checkers.append(False)
    return all(checkers)

def get_user_input(num: int):
    """get input"""
    print("From which box to which do you want to move the number?")
    change = input(">>> ")
    print()
    change_lst = [char for char in change if char != " "]

    if len(change_lst) > 2 or not all(i in " 1234567" for i in change_lst):
        return "\nOnly one move is allowed at a time!\nPlease try again!\n"

    if len(change_lst) < 2:
        return "\nYou entered too few data, try again!\n"

    if change_lst[0] == change_lst[1]:
        return "\nOnly different box numbers are allowed\n"

    change = [change[0], change[1]]

    if len(change) == 2 and change[0].isnumeric() and change[1].isnumeric() and \
0 < int(change[0]) <= num and 0 < int(change[1]) <= num:
        return [int(change[0]), int(change[1])]

    return "\nYou entered data incorrectly\nEnter data in the following format: 12 or 1 2\n"


def main():
    """
    runs the game
    """
    counter_of_victories = 0
    failure, victory = True, False

    for lvl in range(1, 6):
        if counter_of_victories == 5 or not failure:
            continue
        counter_of_failures = 0
        print(f"Your level difficulty is {lvl}/5")
        possible_num = [3, 4, 5, 6, 7]
        num = possible_num[lvl-1]
        boxes = generate_boxes(lvl)
        board_print(boxes, 3 - counter_of_failures, num)


        while counter_of_victories < lvl and failure:
            if counter_of_failures == 3:
                print("LOSS\nYou made too many mistakes")
                failure = False
                continue

            change = get_user_input(num)
            if isinstance(change, str):
                print(change)
                counter_of_failures += 1
                continue
            box_from, box_to = change[0]-1, change[1]-1

            for i, box in enumerate(boxes):

                if i == box_from:  # Check if this is the box we need to pour from
                    if " " in box:
                        idx_1 = box.index(" ") - 1
                    else:
                        if num == 3:
                            idx_1 = num
                        else:
                            idx_1 = num - 1
                    new_item = box[idx_1]

                    try:
                        idx = boxes[box_to].index(" ")
                        boxes[box_to][idx] = new_item
                        del boxes[i][idx_1]
                        boxes[i].append(" ")
                        board_print(boxes, 3 - counter_of_failures, num)
                    except ValueError:
                        counter_of_failures += 1
                        print(f"Box number {box_to + 1} is already full\nTry another move\nYour current HP is {3-counter_of_failures}/3\n")
                    victory = check_for_victory(boxes)
                    if victory:
                        counter_of_victories += 1
                        counter_of_failures = 0
                        break

            if lvl < 5 and victory:
                print(f"\nYou won level {lvl}!\nCONGRATULATIONS!\n But are You smart enough to solve level {lvl+1}?")
                break
            elif lvl == 5 and victory:
                print("You are a genious!")
                break
    if victory:
        print("\n\nYOU WON!\nCONGRATULATIONS!")

print(" Hello, let's play a game\n \
Your task is to move all identical numbers to a single box.\n \
To move a number from box X to box Y, enter XY or X Y.\n \
Only one move is allowed at a time!\n \
If you move a number into a box that is already full 3 times, you lose\n\
Good luck!\n")

if __name__ == '__main__':
    main()
