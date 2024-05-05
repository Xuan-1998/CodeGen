import sys

def solve():
    T = int(input())
    MOD = 10**9 + 7
    
    for _ in range(T):
        N, M, C = map(int, input().split())
        
        # Initialize dp table with zeros
        dp = [0] * (C + 1)
        
        # Calculate the number of different X-sequences
        for i in range(N):
            radius = int(input())
            for j in range(C, radius - 1, -1):
                dp[j] += dp[j - radius]
                if j >= radius:
                    dp[j] %= MOD
        
        for i in range(M):
            radius = int(input())
            for j in range(C, radius - 1, -1):
                dp[j] += dp[j - radius]
                if j >= radius:
                    dp[j] %= MOD
        
        # Print the result
        print(' '.join(map(str, dp)))

if __name__ == "__main__":
    solve()
