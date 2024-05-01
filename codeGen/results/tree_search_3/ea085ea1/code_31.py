def max_common_substrings(str1, str2):
    # Initialize a dictionary to store the count of common non-overlapping substrings
    dp = {(0, 0): 0}

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i-1] == str2[j-1]:
                # If the current characters match, increment the count of common substrings
                dp[(i, j)] = dp.get((i-1, j-1), 0) + 1
            else:
                # If the current characters don't match, start a new substring count
                dp[(i, j)] = 0

    # Find the maximum number of common non-overlapping substrings
    max_count = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                max_count = max(max_count, dp.get((i, j), 0))

    return max_count

# Read input strings from stdin
str1 = input()
str2 = input()

# Print the maximum number of common non-overlapping substrings
print(max_common_substrings(str1, str2))
