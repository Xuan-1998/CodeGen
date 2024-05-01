import sys
from collections import defaultdict

def solve():
    s = input().strip()
    dp = defaultdict(bool)
    for c in s:
        if c == 'A':
            for state, found in list(dp.items()):
                b_count, _ = state
                new_state = (0, b_count + 1)
                if new_state not in dp and s[:s.index('B')].count('B') == b_count + 1:
                    dp[new_state] = True
        elif c == 'B':
            for state, found in list(dp.items()):
                a_count, _ = state
                new_state = (a_count + 1, 0)
                if new_state not in dp and s[:s.index('A')].count('A') == a_count + 1:
                    dp[new_state] = True
    return "YES" if any([found for _, found in dp.values()]) else "NO"

print(solve())
