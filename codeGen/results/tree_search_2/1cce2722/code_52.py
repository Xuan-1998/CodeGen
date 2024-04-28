from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

dp = defaultdict(int)
k = -1
for i in range(n):
    if k != -1 and (a[i] == a[k+1] or a[i] == a[k-1]):
        dp[i] = 1 + min(dp[j] for j in range(max(0, i-2), min(n, i+2)))
    else:
        dp[i] = n
    if a[i] == a[k+1]:
        k += 1
    elif a[i] == a[k-1]:
        k -= 1

print(min(dp.values()))
