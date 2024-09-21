first_num = int(input())
side_len = int(input())

for i in range(side_len):
    for j in range(first_num, first_num + side_len - i):
        if j != first_num: 
            print(" ", end="")
        print(j, end="")
    print() 