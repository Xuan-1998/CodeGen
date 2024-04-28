n = int(input())
s1 = input().strip()
s2 = input().strip()

dp = [[0] * (n+1) for _ in range(n+1)]

max_length = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            max_length = max(max_length, dp[i][j])

ans = 0
i, j = 0, 0
while i < n and j < n:
    if s1[i] == s2[j]:
        i += 1
        j += 1
    elif j > 0 and dp[i][j-1] > 0:
        j -= 1
    else:
        i += 1
    ans = max(ans, dp[i][j])

print(ans)
