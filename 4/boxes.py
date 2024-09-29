"""boxes"""
max_weight = float(input())
uploaded = 0
queue = 0
postponed = 0

while True:
    weights = input()
    if weights=="q":
        break
    try:
        weights = float(weights)
        if weights < 0 or weights == 0:
            postponed += 1
        else:
            if 0 < (max_weight - weights) < max_weight :
                max_weight -= weights
                uploaded += 1
            elif max_weight - weights < 0:
                queue += 1
    except (TypeError, ValueError):
        postponed += 1

print(uploaded)
print(postponed)
print(queue)
