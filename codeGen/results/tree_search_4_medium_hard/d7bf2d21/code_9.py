import sys

def longest_increasing_subsequences(input_array):
    n = len(input_array)
    dp = [1] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            if input_array[i - 1] > input_array[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_length = max(dp)
    count = sum(1 for length in dp if length == max_length)
    return count

input_array = [int(x) for x in sys.stdin.readline().split()]
print(longest_increasing_subsequences(input_array))
