import sys

def solve():
    n, k = map(int, input().split())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]

    dp = [[0] * (1 << k) for _ in range(n)]
    prev_order = 0

    for i in range(n):
        for s in range(1 << k):
            if s != prev_order:
                # Calculate the cost of reversing the current string
                rev_cost = costs[i]
                # Initialize the minimum cost to reverse all strings
                min_cost = sys.maxsize
                for j in range(i + 1, n):
                    # Check if the current string can be inserted into the order s without reversing it
                    if (s >> i) & 1 == ((s >> (j - 1)) & 1):
                        min_cost = min(min_cost, dp[j][s])
                dp[i][s] = min_cost + rev_cost

        prev_order = dp[-1].index(min(dp[-1]))

    return sum(costs) + dp[-1][-1]

print(solve())
