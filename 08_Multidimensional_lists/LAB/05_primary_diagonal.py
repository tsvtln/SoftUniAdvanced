n = int(input())
mx = []
sum = 0

for row in range(n):
    elements = [int(el) for el in input().split()]
    mx.append(elements)

for row_index in range(n):
    sum += mx[row_index][row_index]

print(sum)
