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