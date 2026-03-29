import sys
from collections import defaultdict

# Read input from stdin
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    # Initialize memoization dictionary
    dp = {(1, i): min(9, 10 if i == 0 else i) for i in range(n)}
    for i in range(2, 11):
        dp[(i, 0)] = 0

    # Apply operations and update memoization dictionary
    for _ in range(m):
        new_dp = defaultdict(int)
        for i in range(len(str(n))):
            digit = int(str(n)[i])
            if digit == 9:
                new_dp[1] += dp[(len(str(n)) - i, digit)] + 1
            else:
                new_dp[len(str(n)) - i] = min(10, digit + 1) * (dp.get((len(str(n)) - i, digit), 0) or 1)
        n = int(''.join(map(str, sorted(new_dp)))))
    print(len(str(n)) % (10**9 + 7))
