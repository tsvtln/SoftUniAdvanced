length_n, length_m = map(int, input().split())
numbers_n = set()
numbers_m = set()

for _ in range(length_n):
    numbers_n.add(input())

for _ in range(length_m):
    numbers_m.add(input())

matching = numbers_n.intersection(numbers_m)

print('\n'.join(matching))
