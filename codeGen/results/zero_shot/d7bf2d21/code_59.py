import sys

def initialize_arrays(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp array with ones
    lis_count = 0

    return dp, lis_count

def calculate_dp(arr, dp):
    n = len(arr)
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp

def count_lis(dp, lis_count):
    max_length = max(dp)
    for i in range(len(dp)):
        if dp[i] == max_length:
            lis_count += 1

    return lis_count

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    dp, lis_count = initialize_arrays(arr)
    dp = calculate_dp(arr, dp)
    lis_count = count_lis(dp, lis_count)
    print(lis_count)
