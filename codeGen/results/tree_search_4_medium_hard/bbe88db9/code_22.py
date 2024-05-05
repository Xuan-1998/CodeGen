import sys

def solve():
    n = int(sys.stdin.readline().strip())
    portals = list(map(int, sys.stdin.readline().strip().split()))
    
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        if not dp[i]:
            continue
        
        for j in range(i):
            if portals[j] == i:
                dp[portals[j]] = True
                break

    print(dp[n])

solve()
