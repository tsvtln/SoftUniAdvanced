from collections import deque

quantity_of_food_for_the_day = int(input())
queue_of_orders = deque([int(x) for x in input().split()])
biggest_order = 0

print(max(queue_of_orders))

while queue_of_orders:
    if queue_of_orders[0] <= quantity_of_food_for_the_day:
        quantity_of_food_for_the_day -= queue_of_orders.popleft()
    else:
        break

if not queue_of_orders:
    print('Orders complete')
else:
    print(f"Orders left: {' '.join(map(str, queue_of_orders))}")
