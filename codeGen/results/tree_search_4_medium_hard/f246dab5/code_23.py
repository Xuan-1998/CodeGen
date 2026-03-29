import sys
from collections import defaultdict

def fare_calculator():
    n = int(input())
    dp = [0] * (n + 1)
    prev_tickets = defaultdict(int)

    for i in range(1, n + 1):
        t_i = int(input())
        dp[i] = min((dp[j] or prev_tickets[j]) + (i - j) * 20 for j in range(i))
        prev_tickets[t_i] = dp[i]

    print(*dp[1:], sep='\n')

fare_calculator()
