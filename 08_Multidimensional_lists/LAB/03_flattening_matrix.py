rows = int(input())
matrix = []
flat = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

# for row_index in range(rows):
#     for col_index in range(len(matrix[row_index])):
#         flat.append(matrix[row_index][col_index])

print([el for row in matrix for el in row])

# print(flat)
