def max_common_substrings(str1, str2):
    n = len(str1)
    dp_str1 = [[0] * (n + 1) for _ in range(n + 1)]
    dp_str2 = [[0] * (n + 1) for _ in range(n + 1)]

    # Fill dynamic programming tables
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp_str1[i][j] = dp_str1[i - 1][j - 1] + 1
                dp_str2[i][j] = dp_str2[i - 1][j - 1] + 1

    # Find maximum number of common substrings
    max_count = 0
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            if str1[i - 1] == str2[j - 1]:
                max_count += 1

    return max_count


# Test the function with input strings
str1 = input()
str2 = input()

print(max_common_substrings(str1, str2))
