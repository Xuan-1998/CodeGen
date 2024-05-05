import sys

def longest_increasing_subsequence(input_array):
    n = len(input_array)
    dp = [1] * n  # initialize dp array with ones (subsequences of length 1)

    for i in range(1, n):
        for j in range(i):
            if input_array[i] > input_array[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Read input from stdin
input_array = [int(x) for x in sys.stdin.readline().split()]

print(longest_increasing_subsequence(input_array))
