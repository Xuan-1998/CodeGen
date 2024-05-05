n = int(input())
s = input()
a = [int(x) for x in input().split()]

ways_to_split = 0
max_substring_length = 0
min_substrings = float('inf')

dp = [[False] * (n + 1) for _ in range(26)]

for i in range(n):
    for j in range(i + 1, n + 1):
        for k in range(26):
            if (j - i) <= a[k]:
                dp[k][j] = True

for i in range(26):
    if dp[i][-1]:
        ways_to_split += 1
        max_substring_length = max(max_substring_length, (i + 1) // a[i])
        min_substrings = min(min_substrings, (i + 1) // a[i])

print(ways_to_split % (10**9 + 7))
print(max_substring_length)
print(min_substrings)
