import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

dp = [[0] * (1 << n) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 0

winners = []
for i in range(n):
    prev_sum = dp[i][sum(1 for j in range(i) if s[j] == '1')]
    for j in range(sum(1 for k in range(i+1) if s[k] == '1')), sum(1 for k in range(i+1) if s[k] == '0')]:
        dp[i+1][j] = prev_sum + int(s[i] == '1')
    winners.extend([i for i in range(n) if dp[n][sum(1 for j in range(n) if s[j] == '1')] - prev_sum >= 0])

print(*sorted(winners), sep='\n')
