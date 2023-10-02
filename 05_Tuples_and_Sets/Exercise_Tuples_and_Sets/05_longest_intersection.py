lines = int(input())

longest = set()

for ranges in range(lines):
    first_range, second_range = input().split('-')
    first_start, first_end = first_range.split(',')
