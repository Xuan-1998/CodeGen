n = int(input())  # length of the string s
s = input()  # the string s

a = [int(x) for x in input().split()]  # array a of length 26
cumulative_a = [0] * (len(a) + 1)
for i in range(len(a)):
    cumulative_a[i + 1] = cumulative_a[i] + a[i]

dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][1] = cumulative_a[ord(s[i - 1]) - ord('a')]  # base case
    for j in range(2, min(i + 1, n // a[ord(s[i - 1]) - ord('a')])):
        if s[i - 1] == s[i - j]:
            dp[i][j] = cumulative_a[ord(s[i - 1]) - ord('a')] - cumulative_a[ord(s[i - j]) - ord('a')]
        else:
            dp[i][j] = (dp[i - 1][j - 1] + cumulative_a[ord(s[i - 1]) - ord('a')]) % (10**9 + 7)

num_ways = sum(dp[n][i] for i in range(1, n // max(a) + 2))
longest_substring_length = max(max(row) for row in dp)
min_num_substrings = min(min(row) for row in dp)

print(num_ways % (10**9 + 7))
print(longest_substring_length)
print(min_num_substrings)
