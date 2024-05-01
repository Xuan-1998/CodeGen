def max_common_substrings(str1, str2):
    n = len(str1)
    m = len(str2)

    # Initialize variables to store the maximum number of substrings and the current position in both strings
    max_substrs = 0
    i = j = 0

    while i < n and j < m:
        # Check if there is a common suffix between str1[i:] and str2[j:]
        k = 0
        while i + k < n and j + k < m and str1[i + k] == str2[j + k]:
            k += 1

        # Update the maximum number of substrings
        max_substrs = max(max_substrs, k)

        # Move the sliding window to the next position
        i += k
        j += k

    return max_substrs


# Read input from stdin and print output to stdout
n = int(input())
str1 = input().strip()
str2 = input().strip()

print(max_common_substrings(str1, str2))
