import sys

def longest_increasing_subsequences_count(arr):
    n = len(arr)
    dp = [1] * n
    max_length = 1
    count = 0

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                if dp[i] == max_length:
                    count += 1
                elif dp[i] > max_length:
                    max_length = dp[i]
                    count = 1

    return count

# Read input from stdin
arr = [int(x) for x in sys.stdin.readline().split()]

# Print the result to stdout
print(longest_increasing_subsequences_count(arr))
