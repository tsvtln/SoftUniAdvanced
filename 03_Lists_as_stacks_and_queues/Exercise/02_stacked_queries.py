empty_stack = []
queries = int(input())
for task in range(queries):
    query = input().split()
    if query[0] == '1':
        empty_stack.append(int(query[1]))
    elif empty_stack:
        if query[0] == '2':
            empty_stack.pop()
        elif query[0] == '3':
            print(max(empty_stack))
        elif query[0] == '4':
            print(min(empty_stack))

while empty_stack:
    print(empty_stack.pop(), end='')
    if empty_stack:
        print(', ', end='')
