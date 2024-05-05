dp = {0: 1}
n = int(input())
for i in range(1, n+1):
    dp[i] = sum(dp.get(j, 0) for j in range(i)) if '1' * (i + 1) not in bin(i) else 0

print(sum(dp.values()))
