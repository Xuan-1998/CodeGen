import sys; input = lambda:sys.stdin.readline().strip()

def solve():
    n = int(input())
    MOD = 998244353
    
    dp = [[False for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = True
    
    for i in range(1, n+1):
        for j in range(min(i, n)+1):
            if (i % 2 == 0 and j > 0) or (i % 2 == 1 and j < i):
                dp[i][j] = any(dp[i-1][k] for k in range(max(0, j-1), min(j+1, i)))
    
    print(sum(int(x) for x in str(bin(sum(int(digit == '1' for digit in bin(p)[2:]).count(1))) if digit == '1')) % MOD)

solve()
