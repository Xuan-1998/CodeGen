import sys

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        dp = [[0.0] * 3 for _ in range(n+1)]
        bitmask = [0, 0]
        
        for i in range(1, n+1):
            p1, a1, b1 = map(float, input().split())
            p2, a2, b2 = map(float, input().split())
            
            dp[i][1] = (1 - p1) * max(dp[i-1][0], (1 - p2) * min(1, 1.0 / (i - (bitmask[0] > 0))))
            dp[i][2] = (1 - p2) * max(dp[i-1][0], (1 - p1) * min(1, 1.0 / (i - (bitmask[1] > 0))))
            
            if a1 == a2:
                bitmask[1] = 1
            elif b1 == b2:
                bitmask[0] = 1
        
        print(max(dp[n]))

if __name__ == "__main__":
    solve()
