def length_of_lis(arr):
    dp = [1] * len(arr)  # Initialize dynamic programming table with size equal to array length

    max_length = 0
    for i in range(len(arr)):
        for j in range(i):  # Consider all previous elements
            if arr[i] > arr[j]:  # If current element is greater than the previous one
                dp[i] = max(dp[i], dp[j] + 1)  # Update the length of the longest increasing subsequence ending at the current element
        max_length = max(max_length, dp[i])  # Keep track of the maximum length seen so far

    return max_length

# Example usage:
arr = list(map(int, input().split()))
print(length_of_lis(arr))
