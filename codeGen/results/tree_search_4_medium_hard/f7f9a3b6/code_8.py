codeblock
from collections import defaultdict

n = int(input())
s = input()
a = list(map(int, input().split()))

dp = [defaultdict(int) for _ in range(n)]
ans1 = 0

for i in range(1, n):
    c = s[i-1]
    freq = a[ord(c) - ord('a')]
    for j in range(i-1, -1, -1):
        if i - j <= freq:
            dp[i][j] = max(dp[i][j], dp[j][i-1])
        else:
            break

for i in range(n):
    ans1 += dp[n-1][i]

print(ans1 % (10**9 + 7))

max_len = max((j - i for i, j in enumerate(dp) if dp[-1][j]), default=0)
print(max_len)

min_len = min((j - i for i, j in enumerate(dp) if dp[-1][j]), key=lambda x: (x, s[i:x+1]))
print(min_len + 1)
endcodeblock
