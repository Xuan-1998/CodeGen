def max_points_to_earn(a):
    n = len(a)
    dp = [0] * (n + 1)  # Initialize memoization table

    for i in range(1, n + 1):
        if a[i - 1] % 2 == 0:  # If the current element is even
            dp[i] = max(dp[i - 1], dp[i - 2] + 3) if i >= 2 else 1
        else:  # If the current element is odd
            dp[i] = max(dp[i - 1], dp[i - 1] + 2)

    return dp[-1]

# Example usage:
n = int(input())  # Read the number of elements from stdin
a = list(map(int, input().split()))  # Read the sequence of integers from stdin

print(max_points_to_earn(a))  # Print the maximum number of points that can be earned
