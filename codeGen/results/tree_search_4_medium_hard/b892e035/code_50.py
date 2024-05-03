import sys

# Read the number of test cases
T = int(sys.stdin.readline().strip())

for _ in range(T):
    # Read the number of tickets
    n = int(sys.stdin.readline().strip())

    # Initialize the dp table
    dp = [[0.0 for _ in range(2)] for _ in range(n)]

    # Fill up the dp table
    for i in range(n):
        for j in previous_numbers:
            # Calculate the probability that the current ticket has a certain number (A or B) assigned to it correctly given that the previous number was j
            prob_A = A_prob[i] * (1.0 if prev_num == 0 else dp[i-1][1-A_prob[i]]
            prob_B = B_prob[i] * (1.0 if prev_num == 0 else dp[i-1][1-B_prob[i]]

            # Update the dp table
            dp[i][j] = prob_A + prob_B

    # Print the result
    print(dp[n-1][0])

