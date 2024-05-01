from itertools import combinations

N = int(input())
numbers = [int(x) for x in input().split()]

dp = [[[] for _ in range(N+1)] for _ in range(101)]

for i in range(101):
    dp[i][0] = []

for i in range(1, N+1):
    for j in range(i, 101):
        if j == sum(numbers[:i]):
            dp[i][j] = [j]
        elif dp[i-1][j]:
            dp[i][j] = dp[i-1][j]
        else:
            result = []
            for x in range(1, 101):
                d = j - x
                if i > 1 and dp[i-1][d]:
                    result.extend(dp[i-1][d])
            dp[i][j] = list(set(result))

result_sum = set()
for i in range(N+1):
    for j in range(sum(numbers)+1):
        if dp[i][j]:
            result_sum.update(dp[i][j])

print(*sorted(list(result_sum)), sep=' ')
