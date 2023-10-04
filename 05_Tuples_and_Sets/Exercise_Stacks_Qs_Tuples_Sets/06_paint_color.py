from collections import deque

colors = deque(input().split())
main = ['red', 'blue', 'yellow']
secondary = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['blue', 'yellow']
             }
collected = []

while colors:
    fs = colors.popleft()
    ss = colors.pop() if colors else ''
    if fs + ss in main or fs + ss in secondary:
        collected.append(fs + ss)
    elif ss + fs in main or ss + fs in secondary:
        collected.append(ss + fs)
    else:
        if len(fs) > 1:
            colors.insert(len(colors) // 2, fs[:-1])
        if len(ss) > 1:
            colors.insert(len(colors) // 2, ss[:-1])

for color in collected:
    if color in secondary:
        for el in secondary[color]:
            if el not in collected:
                collected.remove(color)
                break

print(collected)
