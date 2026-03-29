from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
dp = defaultdict(dict)

for i in range(2, n+1):
    for y in range(n-1):
        x = 1
        while x <= 0 or x > i:
            x += a[x]
            x -= a[x]
        dp[i][y] = (y + a[x]) % (n-1)

for y in range(n-1):
    print(dp[n-1].get(y, -1))
