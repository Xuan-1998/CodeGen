import sys
from collections import defaultdict

def calculate_probability():
    T = int(input())
    for _ in range(T):
        n = int(input())
        dp = [0.0] * (n + 1)
        seen = set()
        probabilities = defaultdict(dict)

        for i in range(n):
            p, a, b = map(float, input().split())
            probabilities[a][b] = p
            probabilities[b][a] = p

        dp[0] = 1.0

        for i in range(1, n + 1):
            if len(seen) == i:
                dp[i] = 1.0
            else:
                state_probability = 0.0
                for a in seen:
                    if len(probabilities[a]) > 0:
                        for b in probabilities[a]:
                            state_probability += probabilities[a][b]
                dp[i] = state_probability

        print("{}".format(dp[n]))

calculate_probability()
