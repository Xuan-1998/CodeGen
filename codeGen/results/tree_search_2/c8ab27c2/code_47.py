code = []
from collections import defaultdict

dp = defaultdict(int)

def solve():
    S, T = input().split()
    m, n = len(S), len(T)
    
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                dp[(i, j)] = dp.get((i-1, j-1), 0) + 1
            else:
                dp[(i, j)] = max(dp.get((i-1, j), 0), dp.get((i, j-1), 0))
    
    uncommon_length = float('inf')
    for i in range(m):
        for j in range(n):
            if (i, j) not in dp:
                uncommon_length = min(uncommon_length, m - i)
                break
        else:
            continue
        break
    
    print(-1 if uncommon_length == float('inf') else uncommon_length)

solve()
