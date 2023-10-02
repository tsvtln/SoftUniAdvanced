n = int(input())

cars = set()

for _ in range(n):
    command, number = input().split(', ')
    if command == 'IN':
        cars.add(number)
    elif command == 'OUT':
        cars.remove(number)

if cars:
    for car in cars:
        print(car)
else:
    print('Parking Lot is Empty')