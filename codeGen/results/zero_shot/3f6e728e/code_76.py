import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M, C = map(int, sys.stdin.readline().split())
        upper_radii = sorted(map(int, sys.stdin.readline().split()))
        lower_radii = sorted(map(int, sys.stdin.readline().split()))
        
        # Initialize dp array
        dp = [0] * (C + 1)
        dp[0] = 1
        
        for i in range(C):
            for r in upper_radii:
                if i >= r and dp[i - r]:
                    dp[i] = (dp[i] + dp[i - r]) % (10**9 + 7)
        
        for i in range(C):
            for r in lower_radii:
                if i >= r and dp[i - r]:
                    dp[i] = (dp[i] + dp[i - r]) % (10**9 + 7)
        
        print(' '.join(map(str, dp)))
