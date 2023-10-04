rows, cols = [int(x) for x in input().split()]
mx = [[x for x in input().split()] for _ in range(rows)]

counter = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if mx[row][col] == mx[row][col + 1] == mx[row +1][col] == mx[row + 1][col + 1]:
            counter += 1

print(counter)