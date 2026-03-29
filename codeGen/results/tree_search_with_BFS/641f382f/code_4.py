import sys
import math

def solve(n, a):
    if 1 in a:
        return n - a.count(1)
        
    dp = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
        
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i+length-1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + 1)
            if math.gcd(a[i], a[j]) == 1:
                dp[i][j] = min(dp[i][j], dp[i+1][j-1] + 1)
                
    ans = min(dp[i][j] for i in range(n) for j in range(i, n))
    
    return ans if ans != float('inf') else -1

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    print(solve(n, a))

if __name__ == "__main__":
    main()

