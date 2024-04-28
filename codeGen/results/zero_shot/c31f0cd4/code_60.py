n = int(input())
arr = list(map(int, input().split()))
dp = [[[] for _ in range(n+1)] for _ in range(2**n)]
ans = set()

for i in range(2**n):
    for j in range(n+1):
        if (i & (1 << j)):
            dp[i][j] = dp[i^(1 << j)][j-1] + [arr[j-1]]
        else:
            dp[i][j] = dp[i][j-1]

for i in range(2**n):
    for j in range(n+1):
        if (i & (1 << j)):
            ans.update(set(sum(subset) for subset in dp[i][j]))

print(' '.join(map(str, sorted(list(ans)))))
