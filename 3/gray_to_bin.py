gray = input()
number = int(gray, 2)

len = len(gray)
guessing = number>>(len-1)
if (guessing)&1==1:
    binary = "1"
    counter = 1
else:
    binary = "0"
    counter = 0

for i in range(len-2, -1, -1):
    comp_1 = (number >> i) & 1
    if comp_1==1:
        if counter==1:
            binary+="0"
            counter = 0
        elif counter==0:
            binary+="1"
            counter = 1
    elif comp_1==0:
        if counter==1:
            binary+="1"
            counter = 1
        elif counter==0:
            binary+="0"
            counter = 0

print(binary)
