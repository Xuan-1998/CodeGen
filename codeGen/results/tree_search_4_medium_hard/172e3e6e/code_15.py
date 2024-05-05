def f(k, prev):
    if k == 1:
        return 1
    ans = 0
    for i in range(2, min(k+1, prev)+1):
        if k % i == 0:
            ans += prev // i
    return ans

n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(2, n + 1):
    for j in range(i, -1, -1):
        if a[j-1] % i == 0:
            dp[i] += f(a[j-1], dp[j-1])
    dp[i] %= (10**9 + 7)

print(dp[n]%10**9+7)
