def max_common_substrings(str1, str2):
    N = len(str1)
    common_substrings = set()
    for i in range(N):
        for j in range(i + 1, N + 1):  # Adjust loop bounds for shorter string
            substr = str1[i:j]
            if substr in str2 and substr not in common_substrings:
                common_substrings.add(substr)
    return len(common_substrings)

# Read input from stdin
str1 = input().strip()
str2 = input().strip()

# Print the answer to stdout
print(max_common_substrings(str1, str2))
