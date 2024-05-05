import sys
from collections import deque

def solve():
    n, t = map(int, input().split())
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        q = deque([dp[i - 1]])
        for _ in range(t):
            new_dp = []
            while q:
                grade = q.popleft()
                if i % (10 ** t) // (10 ** (i - 1)) >= 5:
                    new_dp.append(grade + (10 ** (i - 1)))
                else:
                    new_dp.append(grade)
            q = deque(sorted(new_dp, reverse=True))
        dp[i] = max(q)
    
    print(int(str(dp[-1]).rstrip('0').lstrip('0') or '0'))

solve()
