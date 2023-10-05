n = int(input())
mx = []
command = ''

for row in range(n):
    mx.append([int(x) for x in input().split()])

while command != 'END':
    command = input()
    if command == 'END':
        continue
    command = command.split()
    action = command[0]
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])
    if row < 0 or col < 0:
        print('Invalid coordinates')
        continue
    if action == 'Add':
        try:
            mx[row][col] += value
        except IndexError:
            print('Invalid coordinates')
    elif action == 'Subtract':
        try:
            mx[row][col] -= value
        except IndexError:
            print('Invalid coordinates')


for row in mx:
    print(*row, sep=' ')
