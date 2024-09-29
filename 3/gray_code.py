bi_number = input()
number = int(bi_number, 2)

len = len(bi_number)
guessing = number>>(len-1)
if (guessing)&1==1:
    gray = "1"
else:
    gray = "0"
for i in range(len-2, -1, -1):
    count_1 = (number >> i+1) & 1
    count_2 = (number >> i) & 1
    compare = count_1^count_2
    if compare==1:
        gray += "1"
    if compare==0:
        gray += "0"
print(gray)
