import sys
from collections import defaultdict

n, m = map(int, input().split())
plants = [(int(sys.stdin.readline()), float(sys.stdin.readline())) for _ in range(n)]
plants.sort(key=lambda x: x[1])

dp = [0] * n
prev = [-1] * (n + 1)

for i in range(1, n):
    if plants[i][0] != plants[i - 1][0]:
        prev[i] = i
    else:
        count = sum(1 for j in range(i) if plants[j][0] == plants[i][0])
        dp[i] = count

print(dp[-1])
