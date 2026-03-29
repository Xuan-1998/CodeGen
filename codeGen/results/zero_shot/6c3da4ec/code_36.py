import sys

def max_bitwise_or(n, s):
    # Initialize a 2D array to store the results of subproblems
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Fill up the diagonal values (bitwise OR of single characters)
    for i in range(n):
        dp[i][i] = int(s[i])

    # Fill up the upper triangle of the array
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i][i + (length // 2)] | dp[(i + length // 2) + 1][j]
            else:
                dp[i][j] = max(dp[i][i + (length // 2)], dp[(i + length // 2) + 1][j])

    # Return the maximum bitwise OR value
    return bin(max(dp[0][n - 1]))[2:]

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(max_bitwise_or(n, s))
