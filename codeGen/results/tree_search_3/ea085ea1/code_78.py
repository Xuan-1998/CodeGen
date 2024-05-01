def find_max_common_substrings(str1, str2):
    n = len(str1)
    m = len(str2)

    # Initialize the 2D array dp to store whether a substring is common between two strings
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    max_count = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If the current characters match and the substring is common
            if str1[i - 1] == str2[j - 1] and dp[i - 1][j - 1]:
                dp[i][j] = True
                max_count += 1

    return max_count

# Read input from stdin
str1 = input()
str2 = input()

print(find_max_common_substrings(str1, str2))
