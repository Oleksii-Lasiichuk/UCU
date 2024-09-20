first_num = int(input())
second_num = int(input())

len = first_num.bit_length()
distance = 0

for _ in range (len):
    count_1 = first_num & 1
    count_2 = second_num & 1
    if count_1 != count_2:
        distance += 1
    else:
        distance += 0
    first_num = first_num >> 1
    second_num = second_num >> 1

print(distance)


