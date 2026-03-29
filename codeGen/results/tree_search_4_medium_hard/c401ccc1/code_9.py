def zookeeper():
    q = int(input())
    
    # Initialize 2D array for dynamic programming
    dp = [[False] * (1 << 30) for _ in range(1 << 30)]
    
    for _ in range(q):
        u, v = map(int, input().split())
        
        # If there's a path from u to v, print "YES", else print "NO"
        if dfs(u, v, dp):
            print("YES")
        else:
            print("NO")

def dfs(u, v, dp):
    if dp[u][v]:
        return True
    
    for i in range(30):
        w = 1 << i
        if (u & w) == w and not dp[u][w]:
            if dfs(w, v, dp):
                return True
    
    return False

zookeeper()
