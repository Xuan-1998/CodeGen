import sys
from collections import defaultdict

def find_max_common_substrings():
    n = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp1 = [[0] * (n + 1) for _ in range(n + 1)]
    dp2 = [[0] * (n + 1) for _ in range(n + 1)]

    # Initialize the first row and column of both arrays
    for i in range(n + 1):
        dp1[0][i] = dp2[0][i] = 1

    # Fill up the rest of the array using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp1[i][j] = dp1[i - 1][j - 1] + 1
                dp2[i][j] = min(dp1[i - 1][j], dp1[i][j - 1])

    # Calculate the maximum number of common substrings found up to each position in both strings
    max_common_substrings = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp2[i][j] > max_common_substrings:
                max_common_substrings = dp2[i][j]

    print(max_common_substrings)

if __name__ == "__main__":
    find_max_common_substrings()
