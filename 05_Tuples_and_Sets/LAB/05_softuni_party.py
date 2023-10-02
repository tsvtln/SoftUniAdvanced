n = int(input())
reservations = set()
guest = ''

for _ in range(n):
    rev_number = input()
    reservations.add(rev_number)

while guest != 'END':
    guest = input()
    if guest == 'END':
        continue
    reservations.remove(guest)

print(len(reservations))

for num in sorted(reservations):
    print(num)
