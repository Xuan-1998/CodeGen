import sys

def prob_at_least_one_player(n, m, h, s):
    # Calculate the total number of ways to select n players from m departments
    total_ways = 1
    for i in range(1, n+1):
        total_ways *= (m-i+1)

    # Calculate the cumulative sum of dp[i] to get the probability that a randomly formed team will have at least one player from the department of interest
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = sum(dp[j-1] * (m-j) for j in range(1, i+1))
    prob_at_least_one = 1 - sum((dp[i]/total_ways) for i in range(n+1))

    return prob_at_least_one

n, m, h = map(int, input().split())
s = list(map(int, input().split()))
prob = prob_at_least_one_player(n, m, h, s)

print(prob)
