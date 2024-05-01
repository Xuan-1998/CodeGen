def maxCommonSubstrings(str1, str2):
    n = len(str1)
    m = len(str2)

    # Initialize the DP array and memoize values
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    memo = {}

    def dp_helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0 or j == 0:
            result = 0
        elif str1[i - 1] == str2[j - 1]:
            result = dp_helper(i - 1, j - 1) + 1
        else:
            result = max(dp_helper(i - 1, j), dp_helper(i, j - 1))

        memo[(i, j)] = result
        return result

    # Count the maximum number of common non-overlapping substrings
    count = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp_helper(i, j) > 0:
                count += 1

    return count


# Read input from stdin
str1 = input().strip()
str2 = input().strip()

print(maxCommonSubstrings(str1, str2))
