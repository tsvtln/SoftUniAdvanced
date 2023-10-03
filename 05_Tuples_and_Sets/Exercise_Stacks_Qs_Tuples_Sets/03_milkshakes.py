from collections import deque as dq

choco, milk, sd = dq([int(x) for x in input().split(', ')]), dq([int(x) for x in input().split(', ')]), 0

while sd != 5 and milk and choco:

    if milk[0] <= 0 and choco[-1] <= 0:
        milk.popleft()
        choco.pop()
        continue

    if choco[-1] <= 0:
        choco.pop()
        if len(choco) == 0:
            break
        continue

    if milk[0] <= 0:
        milk.popleft()
        if len(milk) == 0:
            break
        continue

    if choco[-1] == milk[0]:
        sd += 1
        choco.pop()
        milk.popleft()

    else:
        milk.rotate(-1)
        choco[-1] -= 5

print("Great! You made all the chocolate milkshakes needed!") if sd >= 5 else print("Not enough milkshakes.")
print(f"Chocolate: {', '.join(map(str, choco))}") if choco else print("Chocolate: empty")
print(f"Milk: {', '.join(map(str, milk))}") if milk else print("Milk: empty")
