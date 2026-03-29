code:
n = int(input())
for _ in range(n):
    k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [0] * (k + 1)
    for i in range(1, len(arr) + 1):
        for j in range(min(i, k), -1, -1):
            dp[j] = max(dp[j], dp[max(0, j-z)] + arr[i-1])
    print(dp[k])
