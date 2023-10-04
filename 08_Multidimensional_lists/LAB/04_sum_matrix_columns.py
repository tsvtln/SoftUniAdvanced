data = input().split(', ')
rows = int(data[0])
cols = int(data[1])

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

for col_index in range(cols):
    sum_col_numbs = 0
    for row_index in range(rows):
        sum_col_numbs += matrix[row_index][col_index]
    print(sum_col_numbs)