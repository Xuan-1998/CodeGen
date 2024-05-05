def solve():
    n, q = map(int, input().split())
    signs = list(input())
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][i] = sum(s - 1 for s in signs[i-1:i]) % 2
        for j in range(i-1, -1, -1):
            if dp[j][i-1]:
                dp[j][i] = (dp[j][i-1] + (signs[j] - 1) % 2)
            else:
                dp[j][i] = min(dp[k][j] for k in range(j+1, i+1)) if j < i else 0
        for j in range(i, n):
            if signs[i-1] == '+' and signs[j] == '-':
                dp[0][j] = min(dp[0][k] + (signs[k] - 1) % 2 for k in range(j+1))
            elif signs[i-1] == '-' and signs[j] == '+':
                dp[0][j] = min(dp[0][k] - (signs[k] - 1) % 2 for k in range(j+1))

    for _ in range(q):
        l, r = map(int, input().split())
        print(min(dp[0][r] - dp[0][l-1]) if l > 0 else 0)

if __name__ == "__main__":
    solve()
