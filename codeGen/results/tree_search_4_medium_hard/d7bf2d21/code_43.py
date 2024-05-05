import sys

def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp array with ones (representing length of longest increasing subsequences ending at each element)

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)  # Update dp[i] if a longer increasing subsequence is found

    max_length = max(dp)
    return sum(1 for x in dp if x == max_length)

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    print(longest_increasing_subsequences(arr))
