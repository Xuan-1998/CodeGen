n = int(input())
a = list(map(int, input().split()))
dp = [0] * (sum(a) + 1)
for x in a:
    for i in range(sum(a), x-1, -1):
        dp[i] += 1
print(*[i for i in range(sum(a) + 1) if dp[i]], sep=' ')
