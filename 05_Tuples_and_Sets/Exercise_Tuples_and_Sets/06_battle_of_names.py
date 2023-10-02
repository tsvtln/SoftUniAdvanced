lines = int(input())

odds = set()
evens = set()

for numbers in range(1, lines + 1):
    name_sum = sum([ord(x) for x in input()]) // numbers
    if name_sum % 2 == 0:
        evens.add(name_sum)
    else:
        odds.add(name_sum)

if sum(odds) == sum(evens):
    result = odds.union(evens)
elif sum(odds) > sum(evens):
    result = odds.difference(evens)
else:
    result = odds.symmetric_difference(evens)

print(*result, sep=', ')
