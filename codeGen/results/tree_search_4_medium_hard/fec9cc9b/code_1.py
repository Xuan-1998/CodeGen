import sys
from collections import defaultdict

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = defaultdict(list)
dp[0].append(0)

for i in range(n):
    for j in range(len(dp[i])):
        if arr[i] >= arr[j]:
            dp[i+1].extend(dp[j])
    dp[i+1].append(i+1)

queries = []
for _ in range(m):
    l, r = map(int, input().split())
    queries.append((l-1, r))

ans = []
for query in queries:
    l, r = query
    if set(arr[l:r+1]) == set(dp[r][r-l+1]):
        ans.append("Yes")
    else:
        ans.append("No")

print(*ans, sep="\n")
