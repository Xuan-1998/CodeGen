code block
import sys

def process_input():
    n = int(input())
    s = input()
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1
    a = [int(x) for x in input().split()]

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, min(i, n - i) + 1):
            if all(freq[ord(c) - ord('a')] <= a[ord(c) - ord('a')] for c in s[i-j:i]):
                dp[i][j] = (dp[i-1][j-1] + 1) % (10**9 + 7)
            else:
                dp[i][j] = dp[i-1][j]

    max_len = 0
    min_substrings = n + 1
    for i in range(n + 1):
        for j in range(i + 1):
            max_len = max(max_len, dp[i][j])
            min_substrings = min(min_substrings, j)
    print((dp[n][n] + 1) % (10**9 + 7))
    print(max_len)
    print(min_substrings)

process_input()
