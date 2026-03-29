import sys
from collections import defaultdict

def solve():
    n = int(input())
    s = input()
    a = list(map(int, input().split()))

    dp = [[0] * (n + 1) for _ in range(27)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(26):
            if s[i].ord() - ord('a') == j:
                if a[j] > 0:
                    a[j] -= 1
                    dp[j][i+1] = max(dp[j][i], dp[j-1][i]) if i and j else dp[0][i]
                    a[j] += 1
                else:
                    dp[j][i+1] = max(0, dp[j-1][i])
            else:
                dp[j][i+1] = max(dp[j-1][i], dp[0][i])
    
    res1 = sum([x[-1] for x in dp])
    res2 = 0
    res3 = float('inf')
    
    for i in range(26):
        res2 = max(res2, dp[i][-1])
        if dp[i][-1] == 0:
            res3 = min(res3, i)
    
    print((res1) % (10**9 + 7))
    print(res2)
    print(res3)

if __name__ == "__main__":
    solve()
