code
from collections import defaultdict

n = int(input())
s = input()
a = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]
ord_to_char = 'abcdefghijklmnopqrstuvwxyz'
char_to_ord = {c: i+97 for i,c in enumerate(ord_to_char)}

for i in range(1, n + 1):
    dp[i][i] = 1
    for j in range(i - 1, -1, -1):
        if all(a[char_to_ord[c.lower()]-97] >= i-j+1 for c in s[j:i]):
            count = sum((dp[k-1][j-1]*a[char_to_ord[s[k].lower()]-97]) for k in range(j, i))
            dp[j][i] = count

count_ways = sum(dp[i][n] for i in range(n+1))
print(count_ways % (10**9 + 7))

max_length = max((j-i+1) for i in range(1, n+1) for j in range(i, n+1) if dp[i][j])
print(max_length)

min_length = min((i-1) for i in range(2, n+1) if sum(dp[j][i-1] for j in range(i)) > 0)
print(min_length)
print()
