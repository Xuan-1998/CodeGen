from collections import defaultdict

mod = 10**9 + 7

dp = defaultdict(int)
dp[0] = 1  # base case: no spheres

for c in range(1, C+1):
    for r in range(C, -1, -1):  # iterate from largest to smallest radius
        dp[r] = (dp[r-1] + dp[r]) % mod

T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    print(*[dp[C-i] for i in range(C+1)], sep=' ')
