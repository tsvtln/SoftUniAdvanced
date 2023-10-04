rows = int(input())
FOUND = False
matrix = []

for row in range(rows):
    matrix.append(list(input()))

searched_elements = input()

for row_index in range(rows):
    if FOUND:
        break
    for col_index in range(len(matrix[row_index])):
        current_elements = matrix[row_index][col_index]
        if current_elements == searched_elements:
            print((row_index, col_index))
            FOUND = True

print(f"{searched_elements} does not occur in the matrix") if not FOUND else None
