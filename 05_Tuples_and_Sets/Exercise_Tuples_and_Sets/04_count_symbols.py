receive_string = input()

count = sorted(set(receive_string))

for char in count:
    print(f"{char}: {receive_string.count(char)} time/s")
