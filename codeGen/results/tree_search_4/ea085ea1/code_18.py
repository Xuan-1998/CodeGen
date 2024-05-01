def max_common_substrings(str1, str2):
    N = len(str1)
    memo = {}

    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0 or j == 0:
            return 0
        
        common = 0
        for k in range(1, min(i + 1, j + 1)):
            if str1[i - k:i] == str2[j - k:j]:
                common += 1
                break
        
        result = helper(i - 1, j) + helper(i, j - 1)
        memo[(i, j)] = max(common, result)
        return memo[(i, j)]

    return helper(N, N)

# Get input from standard input.
str1 = input()
str2 = input()

# Calculate and print the maximum number of common non-overlapping substrings.
print(max_common_substrings(str1, str2))
