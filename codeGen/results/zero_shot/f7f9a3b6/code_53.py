n = int(input())
s = input()
a = [int(x) for x in input().split()]

dp = [[0] * (n + 1) for _ in range(n + 1)]
last = [-1] * (n + 1)
max_length = 0
min_substrings = n

for i in range(n):
    for j in range(i, n):
        if sum([s[k].count(c) % a[ord(c) - ord('a')] for k in range(i, j + 1) for c in set(s[i:j + 1])]) <= a[ord(s[i].lower()) - ord('a')]:
            dp[i][j] = dp[i][i] + 1
        else:
            dp[i][j] = 0

max_length = max(max(dp[i][n - 1] for i in range(n)), default=0)

min_substrings = min(min(i - j + 1 for i in range(n) for j in range(n)) if dp[i][j] > 0 else n for i, j in enumerate(dp))

print(sum(1 for i in range(n) for j in range(n) if dp[i][j]) % (10 ** 9 + 7))
print(max_length)
print(min_substrings)

