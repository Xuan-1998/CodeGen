import sys
input = sys.stdin.read().split('\n')
k, n = map(int, input[0].split())
requests = list(map(int, input[1:]))
group_sizes = [r/1000 for r in requests]
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(k+1):
    dp[0][i] = 0

for j in range(1, n+1):
    for i in range(k+1):
        if i == 0:
            dp[j][i] = 0
        else:
            dp[j][i] = max(dp[j-1][i], sum(min(group_sizes[:j], k)[i] * ci for ci in requests[:j]))

print(str(dp[n][k]))
for j in range(n, -1, -1):
    if dp[j][k] > dp[j-1][k]:
        print(str(j) + ' ' + str(k))
        k -= 1
        break

