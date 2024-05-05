import sys

def infinite_zoo():
    q = int(input())
    dp = [False] * (1 << 30)
    
    for _ in range(q):
        u, v = map(int, input().split())
        
        # Check if there's a path from u to v
        while v > 0:
            if dp[v]:
                print("YES")
                break
            mask = v - 1
            while (u & mask) != mask and not dp[mask]:
                mask -= mask & -mask
            v &= mask
        
        # If no path is found, print "NO"
        else:
            print("NO")

infinite_zoo()
