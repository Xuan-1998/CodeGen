import sys

def solve():
    T = int(sys.stdin.readline().strip())
    
    for _ in range(T):
        N, M, C = map(int, sys.stdin.readline().strip().split())
        
        U = list(map(int, sys.stdin.readline().strip().split()))
        L = list(map(int, sys.stdin.readline().strip().split()))
        
        # Sort the radii in ascending order
        U.sort()
        L.sort()
        
        # Initialize the count of sequences for each possible sequence length
        dp = [0] * (C + 1)
        dp[0] = 1
        
        # For each upper hemisphere, calculate the maximum possible sequence length
        for u in U:
            for i in range(C, u - 1, -1):
                dp[i] = (dp[i] + dp[i - 1]) % (10**9 + 7)
        
        # For each lower hemisphere, update the count of sequences based on the maximum possible sequence length
        for l in L:
            for i in range(C, l - 1, -1):
                dp[i] = (dp[i] + dp[i - 1]) % (10**9 + 7)
        
        # Print the count of sequences for each possible sequence length
        print(*dp)

if __name__ == "__main__":
    solve()
