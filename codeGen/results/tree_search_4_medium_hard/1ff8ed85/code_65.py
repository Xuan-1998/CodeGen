from collections import defaultdict

t = int(input())
dp = defaultdict(int)

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    for i in range(n):
        if i > 0:
            dp[i] = min(dp[j] + (1 if (i % 2 == j % 2 and sum(b[:i]) - sum(b[:j])) <= 10**9 else 0) for j in range(i))
    
    print("YES" if dp[-1] > 0 else "NO")
