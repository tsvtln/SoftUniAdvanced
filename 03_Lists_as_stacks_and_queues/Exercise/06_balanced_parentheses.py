from collections import deque

dq = deque(input())
ob, cb, count = '([{', ')]}', 0

while dq and count < len(dq) / 2:
    if dq[0] not in ob:
        break
    index = ob.index(dq[0])
    if dq[1] == cb[index]:
        dq.popleft()
        dq.popleft()
        dq.rotate(count)
        count = 0
    else:
        dq.rotate(-1)
        count += 1

if dq:
    print('NO')
else:
    print('YES')
