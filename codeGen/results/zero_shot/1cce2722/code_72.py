n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n):
    dp[i] = max(dp[i-1], a[i])
res = 0
while n > 1:
    for i in range(1, n):
        if abs(a[i]-a[0]) == 1:
            res += 1
            j = i
            while j > 0 and (a[j] - a[0]) % 2 == 0:
                dp[j] -= 1
                j -= 1
    n -= 1
print(res)
