import sys
from collections import deque

def min_changes(s, k):
    n = len(s)
    dp = [[False] * (k + 1) for _ in range(n - k + 2)]
    
    for i in range(k - 1, n):
        if s[i - k + 1:i + 1] == 'RGB':
            dp[(i - k + 1) // 3][0] = True
        elif s[i - k + 1:i + 1] == 'BGR':
            dp[(i - k + 2) % 3][0] = True
        elif s[i - k + 1:i + 1] == 'RG':
            dp[(i - k + 1) // 3][0] = True
            
    for i in range(1, n):
        for j in range(k - 1, 0, -1):
            if dp[i][j]:
                if s[i - 1] != 'RGB'[-1]:
                    dp[i - 1][j - 1] = True
                elif s[i - 2] == 'R':
                    dp[(i - 3) // 3][j - 1] = True
                elif s[i - 2] == 'G':
                    dp[(i - 4) % 3][j - 1] = True
                else:
                    dp[(i - 5) // 3][j - 1] = True
                
    min_changes = k
    for i in range(n - k + 1, n):
        if not dp[i][k]:
            break
        min_changes -= 1

    return min_changes

q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    s = input()
    print(min_changes(s, k))
