data = input().split(', ')
rows = int(data[0])
cols = int(data[1])
mx = []

for row in range(rows):
    mx.append([int(x) for x in input().split(', ')])

max_sum = float('-inf')
max_sum_sub_matrix = []

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_elements = mx[row_index][col_index]
        next_element = mx[row_index][col_index + 1]
        element_bellow = mx[row_index + 1][col_index]
        element_diagonal = mx[row_index + 1][col_index + 1]
        sum_elements = current_elements + next_element + element_diagonal + element_bellow

        if max_sum < sum_elements:
            max_sum = sum_elements
            max_sum_sub_matrix = [
                [current_elements, next_element],
                [element_bellow, element_diagonal]
            ]

print(*max_sum_sub_matrix[0], sep=' ')
print(*max_sum_sub_matrix[1], sep=' ')
print(max_sum)