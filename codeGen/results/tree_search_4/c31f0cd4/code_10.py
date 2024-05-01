dp = {}
mem = {0: 0}
max_sum = sum(input().split()) + 1

for t in range(1, max_sum):
    for i in range(len(input().split()), -1, -1):
        if dp.get(i-1, 0) and mem.get(t-i, float('inf')) == 1:
            dp[t] = 1
            break
    else:
        dp[t] = 0

print(*[t for t in range(max_sum) if dp.get(t, 0)], sep=' ')
