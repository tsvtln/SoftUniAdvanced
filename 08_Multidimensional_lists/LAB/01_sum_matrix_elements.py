data = input().split(', ')
rows = int(data[0])
cols = int(data[1])

matrix = []
result = 0

for _ in range(rows):
    elements = [int(el) for el in input().split(', ')]
    matrix.append(elements)

for row in range(rows):
    result += sum(matrix[row])

print(result)
print(matrix)
