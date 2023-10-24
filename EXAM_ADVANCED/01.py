from collections import deque

initial_fuel = [int(x) for x in input().split()]
consumption_indexes = deque(int(x) for x in input().split())
quantities = deque(int(x) for x in input().split())

TOP = False
alt = 0
als = []

while not TOP:
    alt += 1
    fuel_on_hand = initial_fuel.pop()
    wind_factor = consumption_indexes.popleft()
    needed_fuel = quantities.popleft()
    fuel_left = fuel_on_hand - wind_factor
    if fuel_left >= needed_fuel:
        print(f"John has reached: Altitude {alt}")
    else:
        print(f"John did not reach: Altitude {alt}")
        alt -= 1
        break
    if alt == 4:
        TOP = True

if alt > 0 and not TOP:
    print(f"John failed to reach the top. \nReached altitudes: ", end='')
    for altitude in range(1, alt + 1):
        als.append(f"Altitude {altitude}")
    print(', '.join(als))

elif alt == 0:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")

elif TOP:
    print("John has reached all the altitudes and managed to reach the top!")


