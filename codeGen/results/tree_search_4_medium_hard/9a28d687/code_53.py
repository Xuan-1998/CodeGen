import sys
from collections import defaultdict

def solve(n):
    dp = [-1] * (n + 1)
    dp[0] = 0

    costs = {}
    strings = []

    for _ in range(n):
        cost, string = input().split()
        costs[string] = int(cost)

    for i in range(n):
        if dp[i] != -1:
            min_cost = dp[i]
        else:
            sorted_strings = sorted(strings)
            min_cost = float('inf')
            for j in range(i + 1):
                string_cost = costs[sorted_strings[j]]
                reversal_cost = i - j
                total_cost = string_cost + reversal_cost
                if total_cost < min_cost:
                    min_cost = total_cost

        dp[i + 1] = min_cost

    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
