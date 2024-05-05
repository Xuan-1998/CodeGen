from collections import defaultdict

def find_longest_increasing_subsequences(arr):
    dp = [1] * len(arr)  # Initialize DP table
    max_length = 1
    count = defaultdict(int)

    for i in range(len(arr)):
        max_len = 0
        for j in range(i):
            if arr[j] < arr[i]:
                max_len = max(max_len, dp[j])
        dp[i] = max_len + 1
        if dp[i] == max_length:
            count[max_length] += 1
        elif dp[i] > max_length:
            max_length = dp[i]
            count[max_length] = 1

    return sum(count.values())

# Example usage
arr = [5, 4, 2, 3]
print(find_longest_increasing_subsequences(arr))  # Output: 2
