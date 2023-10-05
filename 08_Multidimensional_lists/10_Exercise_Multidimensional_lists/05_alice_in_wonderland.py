n = int(input())
matrix = []
alice = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'A':
            alice = [row, col]
            matrix[row][col] = '*'

possible_moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
tea_bags = 0

while tea_bags < 10:
    command = input()
    move = possible_moves[command]
    row = alice[0] + move[0]
    col = alice[1] + move[1]

    if row < 0 or row >= n or col < 0 or col >= n:
        break
    if matrix[row][col] == 'R':
        matrix[row][col] = '*'
        break
    if matrix[row][col] not in '*.':
        tea_bags += int(matrix[row][col])
    matrix[row][col] = '*'
    alice = [row, col]

if tea_bags >= 10:
    print(f"She did it! She went to the party.")
else:
    print('Alice didn\'t make it to the tea party.')
[print(' '.join(row)) for row in matrix]


# n = int(input())
#
# mx = []
# alice_location = []
# tea_collected = 0
# possible_moves = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1)
# }
#
# for row in range(n):
#     mx.append(input().split())
#     for col in range(n):
#         if mx[row][col] == 'A':
#             mx[row][col] = '*'
#             alice_location = [row, col]
#
# while tea_collected < 10:
#     command = input()
#     move = possible_moves[command]
#     row = alice_location[0] + move[0]
#     col = alice_location[1] + move[1]
#
#     if row < 0 or row >= n or col < 0 or col >= n:
#         break
#     if mx[row][col] == 'R':
#         mx[row][col] = '*'
#         break
#     if mx[row][col] not in '*.':
#         tea_collected += int(mx[row][col])
#     mx[row][col] = '*'
#     alice = [row, col]
#
# if tea_collected >= 10:
#     print(f"She did it! She went to the party.")
# else:
#     print('Alice didn\'t make it to the party.')
# [print(' '.join(row)) for row in mx]
