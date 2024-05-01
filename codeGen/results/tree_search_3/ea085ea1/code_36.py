import sys

def find_max_common_substrings(str1, str2):
    dp = {}
    max_length = len(str1)

    for length in range(1, max_length + 1):
        dp[length] = []
        for i in range(max_length - length + 1):
            substr1 = str1[i:i+length]
            if substr1 in str2:
                dp[length].append((i, length))

    max_common_substrings = 0
    for length in sorted(dp.keys()):
        common_substrings = dp[length]
        max_common_substrings += len(common_substrings)

    return max_common_substrings

# Read input from stdin
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

# Compute and print the result
max_common_substrings = find_max_common_substrings(str1, str2)
print(max_common_substrings)
