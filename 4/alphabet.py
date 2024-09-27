"""alphabet triangle"""

number_of_letters = int(input())

#counting number of rows
back_up_number = number_of_letters
number_of_rows = 0
calculator = 0
remaining = 0
for i in range(1, number_of_letters+1):
    if back_up_number - i > 0:
        back_up_number -= i
        number_of_rows += 1
        calculator += i
    elif back_up_number - i < 0 and i - (number_of_letters-calculator)>0:
        number_of_rows += 1
        remaining = number_of_letters - calculator
        break
    else:
        break

#printing the output
row = 1
current_row = 1
last_letter = 65+number_of_letters-1
letter = 65

while letter <= last_letter:
    if number_of_letters<4:
        print(" " * ((number_of_rows * 2)), end="")
    else:
        print(" " * ((number_of_rows * 2)-2), end="")
    for i in range(row):
        if letter > last_letter:
            break
        if i > 0:
            print(" ", end="")
        print(f"{chr(letter)}", end="")
        letter += 1
    print()
    row += 1
    number_of_rows -= 1

