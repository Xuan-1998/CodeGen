def longest_increasing_subsequence(input_array):
    n = len(input_array)
    dp = [1] * n  # Initialize an array to store the lengths of the longest increasing subsequences

    for i in range(1, n):
        for j in range(i):
            if input_array[i] > input_array[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # Return the maximum value in the dp array

if __name__ == "__main__":
    input_array = [int(x) for x in input().split()]  # Read the input from stdin
    print(longest_increasing_subsequence(input_array))  # Print the length of the longest increasing subsequence
