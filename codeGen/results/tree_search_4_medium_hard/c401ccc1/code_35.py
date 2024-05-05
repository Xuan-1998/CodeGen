import sys

def find_path(q):
    dp = [[False] * (1 << 30) for _ in range(2 ** 30)]
    
    for i in range(2 ** 30):
        dp[i][0] = True
    
    for k in range(1, (1 << 30)):
        for u in range(2 ** 30):
            for v in range(2 ** 30):
                if (u & v) == v and dp[u][k - 1]:
                    dp[v][k] = True
    
    for _ in range(q):
        u, v = map(int, input().split())
        if dp[u][((v ^ u) >> 31)]:
            print("YES")
        else:
            print("NO")

q = int(input())
find_path(q)
