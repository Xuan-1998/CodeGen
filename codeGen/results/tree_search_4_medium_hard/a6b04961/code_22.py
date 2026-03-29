code
def solve():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    
    dp = [[[0] * 2 for _ in range(n+1)] for _ in range(n+1)]
    seen_all = [[False] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, min(i+1, n)+1):
            if not seen_all[i][j]:
                continue
            for k in range(j-1, -1, -1):
                seen_all[k][j] = True
                dp[i][j][0] = max(dp[i][k][0], dp[k][j][0]) + 1
                if j == i:
                    break

    answer = max(max(dp[i][i][0] for i in range(1, n+1)) for _ in range(n+1))
    print(answer)
