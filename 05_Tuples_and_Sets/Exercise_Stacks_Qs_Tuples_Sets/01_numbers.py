from collections import deque

fs, ss, lines = set(map(int, input().split())), set(map(int, input().split())), int(input())

for _ in range(lines):
    inp = deque(input().split())
    command, action = inp.popleft(), inp.popleft()

    if command == 'Add':
        numbers = set(map(int, inp))
        fs.update(numbers) if action == 'First' else ss.update(numbers)

    elif command == 'Remove':
        numbers = set(map(int, inp))
        fs.difference_update(numbers) if action == 'First' else ss.difference_update(numbers)

    elif command == 'Check' and action == 'Subset':
        print('True') if ss.issubset(fs) else print('False')

fs, ss = sorted(fs), sorted(ss)
print(', '.join(map(str, fs))); print(', '.join(map(str, ss)))
