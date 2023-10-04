from collections import deque

rows, cols = [int(x) for x in input().split()]
dq = deque(input())
mx = []

for row in range(rows):
    mx.append([''] * cols)
    for col in range(cols):
        if row % 2 == 0:
            mx[row][col] = dq[0]
        else:
            mx[row][-1 - col] = dq[0]
        dq.rotate(-1)

[print(*row, sep='') for row in mx]
