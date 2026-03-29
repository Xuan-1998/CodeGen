# Read the input
n = int(input())
a = list(map(int, input().split()))

dp = [0] * (10**6 + 1)
for i in range(2, n+1):
    for j in range(i, 0, -1):
        if a[j-1] % j == 0:
            dp[i] += 1
print(dp[-1]%((10**9)+7))
