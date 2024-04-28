def count_subarrays(N, K, Arr):
    dp = [0] * (N + 1)  # Initialize dp array with zeros
    prev_max = 0  # Initialize previous max to 0

    for i in range(1, N + 1):
        if Arr[i - 1] > K:  # If current element is greater than K
            prev_max = max(prev_max, Arr[i - 1])  # Update previous max
            dp[i] = dp[i - 1] + (prev_max > K)  # Count subarrays where max is greater than K
        else:
            dp[i] = dp[i - 1]  # If current element is not greater than K, count remains the same

    return dp[N]

N = int(input())  # Read N from stdin
K = int(input())  # Read K from stdin
Arr = list(map(int, input().split()))  # Read array Arr from stdin
print(count_subarrays(N, K, Arr))  # Print result to stdout
