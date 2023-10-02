input_lines = int(input())
chems = set()

for _ in range(input_lines):
    received = input().split()
    for element in received:
        chems.add(element)

for el in chems:
    print(el)
