import sys
from collections import defaultdict

def solve():
    t = int(input())
    memo = {}

    for _ in range(t):
        n = int(input())
        probs = []
        for _ in range(n):
            p, a, b = map(float, input().split())
            probs.append((p, a, b))

        dp = [(0, 0)]  # Initialize the dynamic programming table
        prob = 1.0  # Initialize the overall probability

        for p, a, b in probs:
            if (a, b) not in memo:
                memo[(a, b)] = 0  # Initialize the memoization value
                dp.append((a, b))  # Add this state to the dynamic programming table
            else:
                dp.append(dp[dp.index((a, b))])  # Avoid redundant calculations

            prob *= p  # Update the overall probability based on the current ticket's probability

        for i in range(len(dp) - 1):
            if (dp[i][0], dp[i+1][1]) not in memo:
                memo[(dp[i][0], dp[i+1][1])] = 0
                prob *= (dp[-1][0] == n and dp[-1][1] == n)

        print(prob)

if __name__ == "__main__":
    solve()
