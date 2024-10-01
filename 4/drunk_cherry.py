"""drunk cherry"""

height = float(input())
weight = float(input())
max_volume = 5 * height * weight
glass, cherries, u_counter, overall_glass = 0, 0, 0, 0

while True:
    action = input()
# new glass
    if action == "U":
        u_counter += 1
        if u_counter == 1:
            pass
        else:
            if not cherries:
                limit_of_cherries = 0
            else:
                limit_of_cherries = 15 / glass * 100
            if glass > 500:
                print("Збій роботи датчика")
                break
            elif glass > max_volume:
                print("Перевищено ліміт алкоголю")
                break
            if limit_of_cherries > 15:
                print("Перевищено ліміт вишень")
                break
        cherries = 0
        overall_glass += glass
        glass = 0
# wine
    elif action[0] == "#":
        if len(action) == 1:
            glass += 20
        else:
            glass += 20 * int(action[2:])
# cherries
    elif action[0] == "0":
        if len(action) == 1:
            glass += 5
            cherries += 5
        else:
            glass += 5 * int(action[2:])
            cherries += 5 * int(action[2:])
# end  q
    elif action == "q":
        overall_glass += glass
        if not cherries:
            limit_of_cherries = 0
        else:
            limit_of_cherries = 15 / glass * 100
        if glass > 500:
            print("Збій роботи датчика")
            break
        elif glass > max_volume:
            print("Перевищено ліміт алкоголю")
            break
        elif limit_of_cherries > 15:
            print("Перевищено ліміт вишень")
            break
        else:
            print(overall_glass)
        break
# checking
    if glass > 500:
        print("Збій роботи датчика")
        break
    elif overall_glass > max_volume or glass > max_volume or overall_glass + glass > max_volume:
        print("Перевищено ліміт алкоголю")
        break
