code block:
def longest_increasing_subsequence(input_array):
    n = len(input_array)
    k_max = max(input_array) - min(input_array) + 1
    dp = [[1] * k_max for _ in range(n)]

    for i in range(1, n):
        for k in range(k_max):
            if input_array[i] > input_array[0]:
                last_increasing_idx = 0
                for j in range(i-1, -1, -1):
                    if input_array[j] <= input_array[0] and input_array[i] - input_array[j] <= k:
                        last_increasing_idx = j
                        break
                dp[i][k] = max(dp[i-1][k], 1 + (dp[last_increasing_idx][k-(input_array[i]-input_array[last_increasing_idx])]) if last_increasing_idx != -1 else 0)
            else:
                dp[i][k] = 1

    return max(max(row) for row in dp)

# Receive input from stdin
n = int(input())

# Initialize the input array
input_array = [int(x) for x in next(iter(sys.stdin)).split()]

print(longest_increasing_subsequence(input_array))
