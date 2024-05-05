from collections import defaultdict

n, q = map(int, input().split())
signs = list(input())

dp = defaultdict(int)
ans = 0

for i in range(n):
    sum_val = sum(signs[i+1:]) if i < n-1 else 0
    dp[sum_val] = min(dp.get(sum_val, float('inf')), 0) if sum_val > 0 else 0

queries = []
for _ in range(q):
    l, r = map(int, input().split())
    for i in range(l-1, -1, -1):
        ans += dp[sum(signs[i:r+1])]
    print(ans)
