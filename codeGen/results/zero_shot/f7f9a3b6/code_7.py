code_block
num_ways = dp[n][n]
longest_substring = 0
min_substrs = n

for i in range(n + 1):
    if all(char_count[c] <= a[ord(c) - ord('a')] for c in s[:i]):
        longest_substring = max(longest_substring, i)
        min_substrs = min(min_substrs, (n - i) // (i + 1))

print(num_ways % (10**9 + 7))
print(longest_substring)
print(min_substrs)
