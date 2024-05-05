code

n = int(input())
s = input()
a = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]
max_length = [[0] * (n + 1) for _ in range(n + 1)]
min_substrings = [[float('inf')] * (n + 1) for _ in range(n + 1)]

dp[0][n - 1] = 1 if all(a[ord(c) - ord('a')] >= len(s[:i]) % a[ord(c) - ord('a')] for i, c in enumerate(s)) else 0

for length in range(1, n + 1):
    for i in range(n - length):
        dp[i][i + length] = sum(dp[i][k] * (dp[k + 1][i + length] if any(a[ord(c) - ord('a')] >= len(s[k:i+length]) % a[ord(c) - ord('a')] for c in s[k:i+length]) else 0 for k in range(i + 1, i + length))
        max_length[i][i + length] = max(max_length[i][k] + len(s[k:i+length]) for k in range(i + 1, i + length)) if any(dp[i][k] for k in range(i + 1, i + length)) else 0
        min_substrings[i][i + length] = min(min_substrings[i][k] + 1 for k in range(i + 1, i + length)) if any(dp[i][k] for k in range(i + 1, i + length)) else float('inf')

print(dp[0][n - 1] % (10 ** 9 + 7))
print(max_length[0][n - 1])
print(min_substrings[0][n - 1])

