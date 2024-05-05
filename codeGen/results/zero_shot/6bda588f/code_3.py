def min_function_value(n, s, a):
    # Initialize a table to store the minimum values for each prefix of the sequence
    dp = [float('inf')] * (n + 1)

    # Base case: F(0) = 0
    dp[0] = 0

    # Iterate over the sequence
    for i in range(n):
        # Calculate the new value for F(i+1)
        dp[i+1] = min(dp[i] + a[i] * (i >= s), dp[i] + a[i-1] * (i < s))

    # Return the minimum value for F(n)
    return dp[n]

t = int(input())  # Read the number of test cases
for _ in range(t):
    n, s = map(int, input().split())  # Read the length and shift values
    a = list(map(int, input().split()))  # Read the sequence
    print(min_function_value(n, s, a))  # Compute and output the minimum value
