field_size = int(input())
field = [input().split() for _ in range(field_size)]
bunny_location = []
rn = 0
cn = 0
max_sum = float('-inf')
max_sum_locations = []
max_direction = ''
temp_sum = 0
move = 0

BUNNY_FOUND = False
for row in field:
    for col in row:
        if col == 'B':
            bunny_location.append(int(rn))
            bunny_location.append(int(cn))
            BUNNY_FOUND = True
            break
        cn += 1
    if BUNNY_FOUND:
        break
    rn += 1
    cn = 0

bunny_location_row = bunny_location[0]
bunny_location_col = bunny_location[1]

# try right
moves_right = field_size - bunny_location[1] - 1
run = 0
for move in range(1, moves_right + 1):
    symbol_field = field[bunny_location_row][bunny_location_col + move]
    if symbol_field.isdigit() or '-' in symbol_field:
        if run == 0:
            temp_sum = int(symbol_field)
        else:
            temp_sum += int(symbol_field)
    elif symbol_field == 'X':
        break
    run += 1
if temp_sum > max_sum:
    max_sum_locations = []
    max_sum = temp_sum
    current_move = bunny_location_col + 1
    max_direction = 'right'
    while current_move < field_size:
        if field[bunny_location_row][current_move] == 'X':
            break
        max_sum_locations.append([bunny_location_row, current_move])
        current_move += 1
#
# temp_sum = 0
#
# try left
move_left = bunny_location_col
run = 0
for move in range(move_left - 1, -1, -1):
    symbol_field = field[bunny_location_row][move]
    if symbol_field.isdigit() or '-' in symbol_field:
        if run == 0:
            temp_sum = int(symbol_field)
        else:
            temp_sum += int(symbol_field)
    elif symbol_field == 'X':
        break
    run += 1
if temp_sum > max_sum:
    max_sum_locations = []
    max_sum = temp_sum
    current_move = bunny_location_col - 1
    max_direction = 'left'
    while current_move >= 0:
        if field[bunny_location_row][current_move] == 'X':
            break
        max_sum_locations.append([bunny_location_row, current_move])
        current_move -= 1

# temp_sum = 0

# try up
move_up = bunny_location_row
run = 0
for move in range(move_up - 1, -1, -1):
    symbol_field = field[move][bunny_location_col]
    if symbol_field.isdigit() or '-' in symbol_field:
        if run == 0:
            temp_sum = int(symbol_field)
        else:
            temp_sum += int(symbol_field)
    elif symbol_field == 'X':
        break
    run += 1
if temp_sum > max_sum:
    max_sum_locations = []
    max_sum = temp_sum
    current_move = bunny_location_row - 1
    max_direction = 'up'
    while current_move >= 0:
        if field[current_move][bunny_location_col] == 'X':
            break
        max_sum_locations.append([current_move, bunny_location_col])
        current_move -= 1

# temp_sum = 0

# try down
move_down = field_size - bunny_location_row - 1
run = 0
for move in range(1, move_down + 1):
    symbol_field = field[bunny_location_row + move][bunny_location_col]
    if symbol_field.isdigit() or '-' in symbol_field:
        if run == 0:
            temp_sum = int(symbol_field)
        else:
            temp_sum += int(symbol_field)
    elif symbol_field == 'X':
        break
    run += 1
if temp_sum > max_sum:
    max_sum_locations = []
    max_sum = temp_sum
    current_move = bunny_location_row + 1
    max_direction = 'down'
    while current_move < field_size:
        if field[current_move][bunny_location_col] == 'X':
            break
        max_sum_locations.append([current_move, bunny_location_col])
        current_move += 1

print(max_direction + '\n' + '\n'.join([str(sublist) for sublist in max_sum_locations]) + '\n' + str(max_sum))


"""
test prints
"""
# print(move_down)
# print(max_direction)
# print(max_sum_locations)
# print(max_sum)
# print(bunny_location)
# print(moves_right)


"""
100/100  functions
"""
# def find_max_direction(field, bunny_location, field_size):
#     max_sum = float('-inf')
#     max_sum_locations = []
#     max_direction = ''
#
#     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#
#     for dr, dc in directions:
#         temp_sum = 0
#         row, col = bunny_location
#
#         while 0 <= row < field_size and 0 <= col < field_size and field[row][col] != 'X':
#             if field[row][col].isdigit():
#                 temp_sum += int(field[row][col])
#             row += dr
#             col += dc
#
#         if temp_sum > max_sum:
#             max_sum = temp_sum
#             max_sum_locations = []
#             row, col = bunny_location
#             while 0 <= row < field_size and 0 <= col < field_size and field[row][col] != 'X':
#                 if (row, col) != bunny_location:
#                     max_sum_locations.append([row, col])
#                 row += dr
#                 col += dc
#             if dr == 0:
#                 if dc == 1:
#                     max_direction = 'right'
#                 else:
#                     max_direction = 'left'
#             else:
#                 if dr == 1:
#                     max_direction = 'down'
#                 else:
#                     max_direction = 'up'
#
#     return max_direction, max_sum_locations, max_sum
#
#
# field_size = int(input())
# field = [input().split() for _ in range(field_size)]
# bunny_location = [(i, row.index('B')) for i, row in enumerate(field) if 'B' in row][0]
#
# direction, locations, max_eggs = find_max_direction(field, bunny_location, field_size)
#
# print(direction + '\n' + '\n'.join([str(sublist) for sublist in locations]) + '\n' + str(max_eggs))
