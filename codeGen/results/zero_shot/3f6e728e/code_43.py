import sys

def solve():
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N, M, C = map(int, sys.stdin.readline().split())
        upper_radii = list(map(int, sys.stdin.readline().split()))
        lower_radii = list(map(int, sys.stdin.readline().split()))
        
        # Sort the radii of both hemispheres
        upper_radii.sort()
        lower_radii.sort()
        
        # Initialize dp array
        dp = [0] * (C + 1)
        dp[0] = 1
        
        for r in range(C):
            if r < N:
                dp[r + 1] += sum(1 for _ in range(len(upper_radii) - i) if upper_radii[i + _] > r) % (10**9 + 7)
            if r < M:
                dp[r + 1] += sum(1 for _ in range(len(lower_radii) - i) if lower_radii[i + _] > r) % (10**9 + 7)
        
        print(*dp, sep=' ')

if __name__ == "__main__":
    solve()
