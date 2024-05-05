def solve():
    n, q = map(int, input().split())
    signs = list(input())
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n):
        if signs[i] == '+':
            dp[i][i] = 0
            for j in range(i):
                dp[i][j] = min(dp[k][j] for k in range(j+1, i)) + (signs[j] == '+' - (signs[i] == '+'))
        else:
            dp[i][i] = 0
            for j in range(i):
                if signs[j] != signs[i]:
                    dp[i][j] = min(dp[k][j] for k in range(j+1, i)) + 1
    res = float('inf')
    for i in range(q):
        l, r = map(int, input().split())
        res = min(res, sum(signs[l-1:r]) % 2)
    print(res)

if __name__ == "__main__":
    solve()
