from math import prod
from functools import reduce

def prob(assigned_numbers):
    # calculate the probability of assigning a new number based on the probabilities of each ticket
    return prod([1 - p if i not in assigned_numbers else p for i, (p, _, _) in enumerate(probs)])

n = int(input())
for _ in range(n):
    n_tickets = int(input())
    probs = []
    for _ in range(n_tickets):
        p, a, b = map(int, input().split())
        probs.append((p, a, b))
    dp = {frozenset([]): 1}
    total_prob = 0
    for i, (p, a, b) in enumerate(probs):
        assigned_numbers = list(dp.keys())[-1]
        new_assigned_numbers = set(assigned_numbers).union({a, b})
        if new_assigned_numbers not in dp:
            dp[new_assigned_numbers] = prob(new_assigned_numbers)
        total_prob += dp[set(assigned_numbers)] * p
    print(round(total_prob, 6))
