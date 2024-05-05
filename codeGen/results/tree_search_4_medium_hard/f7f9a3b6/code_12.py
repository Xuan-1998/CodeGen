import sys

n = int(input())
s = input()
a = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(i - 1, -1, -1):
        if s[j:i].isalpha() and i - j <= a[ord(s[j-1])-97]:
            dp[i][j] = sum(dp[k][j - 1] * a[ord(s[k-1])-97] for k in range(j, i)) + (dp[i-1][j-1] if i > 0 else 1)
        else:
            dp[i][j] = 0

ways_to_split = sum(dp[n][i] for i in range(n + 1))
print((ways_to_split % (10**9 + 7)), flush=True)

dp_max_length = max(max(k) for k in dp)
min_substrings = min(min(len(list(x)) for x in dp))

print(dp_max_length, flush=True)
print(min_substrings, flush=True)
