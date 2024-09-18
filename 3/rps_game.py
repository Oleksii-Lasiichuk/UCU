# while True:
#     comb = input()
#     if comb == '':
#         break
#     else:
#         if comb in ["PS", "RP", "SR"]:
#             print("False")
#         elif comb in ["SP", "PR", "RS"]:
#             print("True")
#         else:
#             print("False|False")
    
while True:
    comb = input()
    match comb:
        case "PS" | "RP" | "SR":
            print("False")
        case "SP" | "PR" | "RS":
            print("True")
        case _:
            print("False | False")
    