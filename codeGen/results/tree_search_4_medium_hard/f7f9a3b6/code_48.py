def process_input():
    n = int(input())
    s = input()
    a = [int(x) for x in input().split()]
    return n, s, a

n, s, a = process_input()

dp = [[0] * (max(a) + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    count = 0
    j = 0
    while j < i:
        if count >= a[ord(s[j]) - ord('a')]:
            dp[i][j] = max(dp[k-1][min(j, count)] + 1 for k in range(1, j+1))
        else:
            dp[i][j] = dp[i-1][j]
        j += 1
        if s[j-1] == s[j]:
            count += 1
        else:
            count = 0

print(dp[n].index(max(dp[n])))
