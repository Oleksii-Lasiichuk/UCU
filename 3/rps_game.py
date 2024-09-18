while True:
    comb = input()
    if comb == '':
        break
    else:
        if comb in ["PS", "RP", "SR"]:
            print("False")
        elif comb in ["SP", "PR", "RS"]:
            print("True")
        else:
            print("False|False")
    