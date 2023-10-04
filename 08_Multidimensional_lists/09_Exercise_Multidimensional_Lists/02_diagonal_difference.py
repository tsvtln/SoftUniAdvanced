n = int(input())
mx = [[int(x) for x in input().split()] for _ in range(n)]

primary = [mx[i][i] for i in range(n)]
secondary = [mx[i][-i - 1] for i in range(n)]

print(abs(sum(primary) - sum(secondary)))
