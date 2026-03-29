from collections import namedtuple

Result = namedtuple('Result', 'x y')

def solve():
    A, B = map(int, input().split())
    
    dp = [[float('inf')] * (B + 1) for _ in range(A + 1)]
    dp[0][0] = 0
    
    for a in range(1, A + 1):
        for b in range(bmax := min(B, a)):
            if a - b >= 2 and dp[a - 2 * (a - b)][b]:
                dp[a][b] = min(dp[a][b], 2 * (a - b) + 1)
    
    if dp[A][B] == float('inf'):
        print(-1)
    else:
        x, y = A - B // 2, B % 2
        print(Result(x, y))
