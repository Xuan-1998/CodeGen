_code_
from collections import defaultdict

def solve():
    n = int(input())
    s = input()
    
    dp = [[0, 0]] * (n + 1)
    dp[0] = [0, 0]
    
    for i in range(1, n):
        prev_color = 'R' if s[i - 1] == 'G' else ('G' if s[i - 1] == 'B' else 'B')
        if (s[i] != prev_color) and ((dp[i - 1][0] + 1, dp[i - 1][1]) or (dp[i - 1][0], dp[i - 1][1] + 1)):
            dp[i] = [(dp[i - 1][0] + 1, dp[i - 1][1])]
        else:
            dp[i] = [dp[i - 1]]
    
    r = len(dp[-1])
    t = ''.join(['R' if i % 2 == 0 else ('G' if (i // 2) % 3 == 0 else 'B') for i in range(n)])
    
    print(r)
    print(t)

solve()
_code_
