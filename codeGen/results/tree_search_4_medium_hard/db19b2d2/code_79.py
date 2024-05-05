import sys

def prob_at_least_one_player(s, n, h):
    # Initialize dp array to store probabilities for each number of players (0 to n)
    dp = [0] * (n + 1)

    # Calculate the cumulative sum of players in the desired department
    cum_sum = 0
    for i in range(1, m + 1):
        cum_sum += s[i - 1]
        if i == h:
            break

    # Fill up the dp array using a bottom-up approach
    for i in range(n + 1):
        if i < s[h - 1]:
            dp[i] = 0.0
        else:
            # Calculate the probability of forming a team with at least one player from the department of interest
            if cum_sum > i:
                dp[i] = (cum_sum - i) / cum_sum
            elif cum_sum == i:
                dp[i] = 1.0
            else:
                # No way to form a team with at least one player from the department of interest
                dp[i] = 0.0

    return dp[n]

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Calculate and print the probability
print(prob_at_least_one_player(s, n, h))
