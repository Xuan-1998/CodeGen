import sys
input()

n = int(input())
s = input().strip()
a = [int(x) for x in input().split()]

dp = [[0] * (max(a)+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(1, n+1):
    c = s[i-1]
    for j in range(max(a), -1, -1):
        dp[i][j] = sum(dp[k][j-1] * dp[i-k-1][min(j-1, a[ord(c)-97])] for k in range(i))
    if i > 0:
        c = s[i-1]
        a_val = a[ord(c)-97]
        for j in range(a_val+1):
            dp[i][j] += dp[i-1][min(j, a_val)]

ans = sum(dp[i][-1] for i in range(n+1))
print(ans % (10**9 + 7))

longest_substring_length = max(max(row) for row in dp)
print(longest_substring_length)

min_num_substrs = min(i for i in range(n+1) if dp[i][-1] == 0)
print(min_num_substrs)
