def max_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    # Create a dictionary to store the DP values
    dp = {}

    def dfs(i, j):
        if (i, j) in dp:
            return dp[(i, j)]

        # If the current characters match and we haven't exceeded the length of the strings
        if i < N and j < N and str1[i] == str2[j]:
            # Update the DP value with the maximum number of common non-overlapping substrings
            dp[(i, j)] = dfs(i+1, j+1) + 1
        else:
            dp[(i, j)] = max(dfs(i-1, j), dfs(i, j-1))

        return dp[(i, j)]

    # The maximum number of common non-overlapping substrings is the maximum value in the DP table
    print(dfs(N-1, N-1))
