import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    DP = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            if arr[j] < arr[i]:
                DP[i] = max(DP[i], DP[j] + 1)
            else:
                DP[i] = DP[i]

    return max(DP)

# Read input from stdin
arr = [int(x) for x in sys.stdin.readline().split()]

# Calculate and print the answer
print(longest_increasing_subsequence(arr))
