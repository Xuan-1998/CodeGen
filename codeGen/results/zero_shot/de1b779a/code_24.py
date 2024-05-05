# Initialize a table to store the maximum profit for each amount of dough
dp = [0] * (n + 1)

for i in range(1, n + 1):
    # Calculate the maximum profit for each amount of dough
    for stuffing in stuffings:
        if i >= stuffing['ci']:
            dp[i] = max(dp[i], dp[i - stuffing['ci']] + stuffing['di'])
    if i < c0:
        dp[i] = d0

# Print the maximum profit
print(max_profit)
