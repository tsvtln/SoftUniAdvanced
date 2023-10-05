n = int(input())

mx = []
knights = []

for row in range(n):
    mx.append([x for x in input()])
    for col in range(n):
        if mx[row][col] == 'K':
            knights.append([row, col])

removed_knights = 0
possible_moves = [
    (1, 2),
    (2, 1),
    (-1, 2),
    (-2, 1),
    (1, -2),
    (2, -1),
    (-1, -2),
    (-2, -1)
]

while True:
    max_hits = 0
    max_knight = [0, 0]
    for knight_row, knight_col in knights:
        hits = 0
        for move in possible_moves:
            new_row = knight_row + move[0]
            new_col = knight_col + move[1]
            if 0 <= new_row < n and 0 <= new_col < n:
                if mx[new_row][new_col] == 'K':
                    hits += 1
        if hits > max_hits:
            max_hits = hits
            max_knight = [knight_row, knight_col]
    if max_hits == 0:
        break
    knights.remove(max_knight)
    mx[max_knight[0]][max_knight[1]] = '0'
    removed_knights += 1

print(removed_knights)
