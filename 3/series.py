len = int(input())
series = ""
operation = True
for i in range (1, len*2+1, 2):
    series += f"{i}/{i+1}"
    if i+1 == len*2:
        pass
    else:
        if operation==True:
            series += " - "
        else:
            series += " + "
    operation = not operation
print(series)

