code
from collections import defaultdict

def calculate_final_y(n, seq):
    dp = defaultdict(int)
    for x in range(1, n+1):
        while x > 0 and x <= n:
            y = dp[(x-1, x)]
            x -= seq[x]
            y += seq[x]
        if x <= 0 or x > n:
            break
        dp[(x, y)] = y
    return [-1] + [dp[i] for i in range(2, n+1)]

n = int(input())
seq = list(map(int, input().split()))
print('\n'.join(map(str, calculate_final_y(n, seq))))
