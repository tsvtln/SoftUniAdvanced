mx = []
position = []
targets = 0

for row in range(5):
    mx.append(input().split())
    for col in range(5):
        if mx[row][col] == 'A':
            position = [row, col]
        elif mx[row][col] == 'x':
            targets += 1

directions = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
targets_down = []

number_of_commands = int(input())

for i in range(number_of_commands):
    command = input().split()
    if command[0] == 'shoot':
        row = position[0] + directions[command[1]][0]
        col = position[1] + directions[command[1]][1]
        while 0 <= row < 5 and 0 <= col < 5:
            if mx[row][col] == 'x':
                mx[row][col] = '.'
                targets -= 1
                targets_down.append([row, col])
                break
            row += directions[command[1]][0]
            col += directions[command[1]][1]
        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break
    elif command[0] == 'move':
        steps = int(command[2])
        direction = command[1]
        if direction == 'up':
            row = position[0] - steps
            col = position[1]
        elif direction == 'down':
            row = position[0] + steps
            col = position[1]
        elif direction == 'left':
            row = position[0]
            col = position[1] - steps
        else:
            row = position[0]
            col = position[1] + steps
        if 0 <= row < 5 and 0 <= col < 5 and mx[row][col] == '.':
            mx[row][col] = 'A'
            mx[position[0]][position[1]] = '.'
            position = [row, col]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")
[print(row)for row in targets_down]
