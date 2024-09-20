g1 = int(input())
g2 = int(input())
g3 = int(input())
g4 = int(input())
g5 = int(input())
average_g = (g1+g2+g3+g4+g5)/5
if 0<=g1<=100 and 0<=g2<=100 and 0<=g3<=100 and 0<=g4<=100 and 0<=g5<=100:
    match average_g:
        case _ if 100 >= average_g >= 90:
            print(f"Average grade = {average_g:.1f} -> A")
        case _ if 90 > average_g >= 80:
            print(f"Average grade = {average_g:.1f} -> B")
        case _ if 80 > average_g >= 75:
            print(f"Average grade = {average_g:.1f} -> C")
        case _ if 75 > average_g >= 65:
            print(f"Average grade = {average_g:.1f} -> D")
        case _ if 65 > average_g >= 60:
            print(f"Average grade = {average_g:.1f} -> E")
        case _ if average_g < 60:
            print(f"Average grade = {average_g:.1f} -> F")
else:
    print(None)