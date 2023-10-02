receive = tuple(float(x) for x in input().split())

count = {}
for number in receive:
    count[number] = receive.count(number)

for key, value in count.items():
    print(f"{key} - {value} times")

