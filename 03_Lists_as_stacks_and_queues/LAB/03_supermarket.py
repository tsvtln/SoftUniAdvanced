from collections import deque

customer_list = deque()
name = input()

while name != 'End':
    if name == 'Paid':
        while customer_list:
            print(customer_list.popleft())
    else:
        customer_list.append(name)
    name = input()
print(f"{len(customer_list)} people remaining.")
