from collections import defaultdict

def min_replants(n, m):
    memo = {}

    def dp(plants):
        if plants == 0:
            return 0

        state = tuple(sorted((i, s) for i, (_, s) in enumerate(plants)))
        if state in memo:
            return memo[state]

        # Initialize the minimum cost
        min_cost = float('inf')

        # Consider two possible actions: place a border or don't
        for i in range(m - 1):
            left, right = plants[:i], plants[i:]
            left_cost = dp(left)
            right_cost = dp(right)

            # Calculate the minimum cost by considering all possible borders
            min_cost = min(min_cost, left_cost + (right_cost if i == m - 2 else 0))

        memo[state] = min_cost
        return min_cost

    plants = [(i, s) for i, (_, s) in enumerate(map(int, input().split()))]
    print(dp(n))
