n = int(input())
s = input()
a = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = (dp[i - 1] + 1) if s[i - 1] in 'abcdefghijklmnopqrstuvwxyz' else dp[i - 1]

ways = 0
max_length = 0

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if all(s[k - a[ord(c) - ord('a')]] <= c for k in range(j, i, -1)):
            ways += 1
            max_length = max(max_length, j - i)

min_substrings = float('inf')
for i in range(1, n + 1):
    for j in range(i, n + 1):
        if all(s[k - a[ord(c) - ord('a')]] <= c for k in range(j, i, -1)):
            min_substrings = min(min_substrings, j - i)

print(ways % (10 ** 9 + 7))
print(max_length)
print(min_substrings)
