from collections import deque

circle, sp, visits = int(input()), 0, 0
petrol_pumps = deque([])

for g in range(circle):
    amount_of_petrol, distance_to_next_pump = map(int, input().split())
    petrol_pumps.append([amount_of_petrol, distance_to_next_pump])

while visits < circle:
    fuel = 0
    for ind in range(circle):
        fuel += petrol_pumps[ind][0]
        destination = petrol_pumps[ind][1]
        if fuel < destination:
            petrol_pumps.rotate(-1)
            sp += 1
            visits = 0
            break
        fuel -= destination
        visits += 1

print(sp)

# from collections import deque
# gas_stations = int(input())
# stations = ([])
# fuel = 0
#
# for station_info in range(gas_stations):
#     # amount_of_petrol, distance_to_next_pump = map(int, input().split())
#     current_info = [int(x) for x in input().split()]
#     stations.append(current_info)
#
# for fuel in range(gas_stations):
#     if stations[0][0] >= stations[0][1]:
#         fuel += stations
