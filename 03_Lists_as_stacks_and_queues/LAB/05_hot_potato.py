from collections import deque

children = deque(input().split())

n = int(input()) - 1

while len(children) != 1:
    children.rotate(-n)
    print(f"Removed {children.popleft()}")

print(f"Last is {children.popleft()}")
