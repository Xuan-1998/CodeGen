import sys
from collections import defaultdict

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[0] * (q+1) for _ in range(n+1)]
    
    prefix_sum = 0
    sign_count = defaultdict(int)

    for i in range(1, n+1):
        if signs[i-1] == "+":
            sign_count[1] += 1
        else:
            sign_count[-1] += 1

        prefix_sum += 2*sign_count[1] - 2*sign_count[-1]
        
    for i in range(1, n+1):
        dp[i][0] = abs(prefix_sum)
    
    for j in range(1, q+1):
        l, r = map(int, input().split())
        sign_sum = 2*sign_count[1] - 2*sign_count[-1]
        
        if (r-l+1) % 2 == 0:
            dp[l][j] = min(dp[l-1][j-1], abs(sign_sum))
        else:
            dp[l][j] = min(abs(prefix_sum - sign_sum), dp[l-1][j-1])
    
    print(dp[n][q])

if __name__ == "__main__":
    solve()
