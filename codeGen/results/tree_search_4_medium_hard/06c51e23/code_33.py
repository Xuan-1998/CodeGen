def max_grade(n, t):
    dp = [0] * (n + 1)  # Initialize dynamic programming table

    for i in range(1, n + 1):  # Iterate over each digit after decimal point
        if i <= 5:
            dp[i] = int((10 ** (i - 1)) * 5.0)  # Round down to nearest integer
        else:
            dp[i] = int((10 ** (i - 1)) * 6.0)  # Round up to nearest integer

    return sum(dp)  # Return the total grade

n, t = map(int, input().split())  # Read input from stdin
print(max_grade(n, t))  # Print the answer to stdout
