"""alphabet triangle"""
number_of_letters = int(input())

#counting number of raws
back_up_number = number_of_letters
counter = 0
calculator = 0
remaining = 0
for i in range(1, number_of_letters):
    if back_up_number - i > 0:
        back_up_number -= i
        counter += 1
        calculator += i
    elif back_up_number - i < 0 and i - (number_of_letters-calculator)>0:
        counter += 1
        remaining = (number_of_letters - calculator)
        break
    else:
        break



# if number <= 25:
#     for i in range(number):
#         for j in range(65, 66+number):
#             print(" "*number,chr(j))



