n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (sum(arr) + 1)
for x in arr:
    for i in range(sum(arr), x - 1, -1):
        dp[i] += 1
print(' '.join(str(i) for i in set(dp)))
