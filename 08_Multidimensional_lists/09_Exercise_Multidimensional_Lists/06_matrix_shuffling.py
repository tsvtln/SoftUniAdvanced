rows, cols = [int(x) for x in input().split()]
mx = [[x for x in input().split()] for _ in range(rows)]
line = ''


def validator(r1, c1, r2, c2, rws, cls):
    return 0 <= r1 < rws and 0 <= r2 < rws and 0 <= c1 < cls and 0 <= c2 < cls


while line != 'END':
    line = input()
    if line == 'END':
        continue
    command = line.split()
    if command[0] != 'swap' or len(command) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]
    if validator(row1, col1, row2, col2, rows, cols):
        mx[row1][col1], mx[row2][col2] = mx[row2][col2], mx[row1][col1]
        [print(*row) for row in mx]
    else:
        print("Invalid input!")
