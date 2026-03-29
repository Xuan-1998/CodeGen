import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # initialize table with ones, since each element is its own increasing subsequence of length 1

    for i in range(1, n):
        for j in range(i):  # consider all previous elements
            if arr[i] > arr[j]:  # check if current element is greater than the previous one
                dp[i] = max(dp[i], dp[j] + 1)  # update the length of the longest increasing subsequence ending at i

    return max(dp)

# Read input from stdin
arr = [int(x) for x in sys.stdin.readline().split()]

# Print the answer to stdout
print(longest_increasing_subsequence(arr))
