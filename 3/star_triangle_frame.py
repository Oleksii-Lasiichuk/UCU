a = int(input())
count=1
if a<=3:
    for i in range (1, a+1):
        print("*"*i)
elif a>3:
    print("*")
    print("**")
    for i in range(a-3):
        print(f"*{" "*count}*")
        count+=1
    print("*"*a)

