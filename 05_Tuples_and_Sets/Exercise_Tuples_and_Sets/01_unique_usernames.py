cycle = int(input())

unique_names = set()

for _ in range(cycle):
    name = input()
    unique_names.add(name)

for name in unique_names:
    print(name)