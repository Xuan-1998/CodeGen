import sys

def solve(n, s, a):
    ways = 0
    longest_substring_length = 0
    min_substrings = float('inf')

    dp = [[0] * 26 for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(26):
            if s[i - 1].lower() == chr(j + ord('a')):
                dp[i][j] = min(dp[i - 1][j], a[j])
            else:
                dp[i][j] = dp[i - 1][j]
            dp[i][ord(s[i - 1].lower()) - ord('a')] += dp[i - 1][ord(s[i - 1].lower()) - ord('a')]

    for i in range(n):
        if dp[n][ord(s[i].lower()) - ord('a')] > 0:
            ways += 1
            longest_substring_length = max(longest_substring_length, i + 1)
            min_substrings = min(min_substrings, i + 1)

    return ways % (10**9 + 7), longest_substring_length, min_substrings

# Read input from stdin
n = int(input())
s = input()
a = [int(x) for x in input().split()]

# Solve the problem and print output to stdout
ways, longest_substring_length, min_substrings = solve(n, s, a)
print(ways, file=sys.stdout)
print(longest_substring_length, file=sys.stdout)
print(min_substrings, file=sys.stdout)
