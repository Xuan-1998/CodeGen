import sys
from collections import defaultdict

def solve(t, s):
    n = len(s)
    dp = [[-1 for _ in range(n+1)] for _ in range(len(t)+1)]
    
    used_strs = set()
    used_pos = 0
    
    for i in range(len(t)-1, -1, -1):
        for j in range(n-1, -1, -1):
            if s[j] not in t[i:]:
                dp[i][j] = -1
                continue
            
            w_j = j
            p_j = i
            while w_j >= 0 and p_j >= 0:
                if t[p_j:w_j+1] == s[w_j]:
                    used_strs.add(w_j)
                    used_pos = max(used_pos, p_j)
                    break
                p_j -= 1
                w_j -= 1
            
            dp[i][j] = dp[used_pos][w_j-1] if (used_pos, w_j-1) in memo else min(dp[used_pos][w_j-1], dp[i-1][j-1]+1)
    
    return dp[0][n-1]

memo = defaultdict(int)

t = input().strip()
n = int(input())
s = [input().strip() for _ in range(n)]

m = solve(t, s)
if m == -1:
    print(-1)
else:
    used_strs = set([i for i in range(len(s)) if i not in used_strs])
    for j in range(m):
        w_j = min(used_strs)
        p_j = t.index(s[w_j])
        print(w_j+1, p_j+1)
        used_strs.remove(w_j)
