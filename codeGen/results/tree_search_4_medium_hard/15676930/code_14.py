# Read inputs from standard input
n = int(input())
a_values = list(map(int, input().split()))
b_values = list(map(int, input().split()))
c_values = list(map(int, input().split()))

# Check for valid inputs
if any(val > 10**5 or val < 0 for val in a_values + b_values + c_values):
    print("Invalid input!")
else:
    # Initialize the dynamic programming table
    dp = [[0] * (n+1) for _ in range(n+1)]

    # Fill up the table row by row, starting from i=1 and j=1
    for i in range(1, n+1):
        for j in range(min(i, n)+1):
            if j == 0:  # First hare has no adjacent full hares
                dp[i][j] = a_values[0]
            elif j == i:  # Last hare has all adjacent hares full
                dp[i][j] = c_values[-1]
            else:
                dp[i][j] = max(dp[i-1][j], b_values[j-1])

    # The maximum total joy is the value in the bottom-right corner of the table
    print(dp[-1][-1])
