from collections import deque
clothes = deque([int(x) for x in input().split()])
capacity = int(input())

current_rack = 0
racks = 0

while clothes:
    current_box = clothes[0]
    if current_rack + current_box <= capacity:
        current_rack += clothes.popleft()
    elif current_rack + current_box > capacity:
        racks += 1
        current_rack = clothes.popleft()
    if len(clothes) == 1:
        racks += 1

print(racks)
