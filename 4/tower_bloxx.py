"""tower of bloxx"""

number_of_blocks = 1
start_of_block = 1
start_of_next_block = 1
points = 15
block = input()
while points > 0:
    next_block = input()
    difference = 0
    hashtag_reached_block = False
    hashtag_reached_next_block = False
    for i in block:    
        if i == ".":
            if not hashtag_reached_block:
                start_of_block += 1
        elif i == "#":
            hashtag_reached_block = True
    for i in next_block:    
        if i == ".":
            if not hashtag_reached_next_block:
                start_of_next_block += 1
        else:
            hashtag_reached_next_block = True
    if start_of_block != start_of_next_block:
        difference = abs(start_of_block - start_of_next_block)
        if difference >= 3:
            points -= 3
            start_of_block = 1
            start_of_next_block = 1
        elif difference == 2 or difference == 1:
            points -= difference
            block = next_block
            number_of_blocks += 1
            start_of_block = 1
            start_of_next_block = 1
    else:
        block = next_block
        number_of_blocks += 1
        start_of_block = 1
        start_of_next_block = 1
print(number_of_blocks)

            



        
    # points = 15
# # start_of_block = 1
# # block = input()
# # for i in block:    
# #     if i == ".":
# #         start_of_block += 1
# #     elif i == "#":
# #         pass
# number_of_blocks = 2
# block = input()
# while points > 0:
#     next_block = input()
#     counter = 0
#     for i in range(9):
#         if block[i] == next_block[i]:
#             pass
#         elif block[i] != next_block[i]:
#             if block[i+1] != next_block[i+1]:
#                 counter += 1
#             if counter >= 3:
#                 next_block = input()
#                 break
#             else:
#                 block = next_block
#                 next_block = input()
#                 number_of_blocks += 1
#     print(points)
#     points -= counter
#     if points<=0:
#         print(number_of_blocks)
#         break
#     else:
#         continue
