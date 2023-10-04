n = int(input())
mx = [[int(x) for x in input().split(', ')] for _ in range(n)]

primary = [mx[i][i] for i in range(n)]
secondary = [mx[i][n - i - 1] for i in range(n)]

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")
