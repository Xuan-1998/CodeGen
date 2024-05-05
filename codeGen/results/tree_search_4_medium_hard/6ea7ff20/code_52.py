import sys
from math import floor

n = int(input())
p = list(map(int, input().split()))

dp_sum_even = [0] * (n + 1)
dp_sum_odd = [0] * (n + 1)

for i in range(2 * n):
    if i % 2 == 0:
        dp_sum_even[i // 2 + 1] += p[i]
    else:
        dp_sum_odd[i // 2 + 1] += p[i]

dp = [[False] * (floor((n - i) / 2) + 1) for i in range(n)]

for i in range(n):
    for j in range(min(i, floor((n - i) / 2)) + 1):
        if dp_sum_even[i] <= dp_sum_odd[j]:
            dp[i][j] = True
        else:
            break

print("YES" if any(all(dp[i][j]) for i in range(n)) else "NO")
