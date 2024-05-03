import sys

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        probs = []
        for _ in range(n):
            p1, num1, num2 = map(float, input().split())
            probs.append((p1, num1, num2))
        dp = [[0.0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1.0
        for i in range(1, n + 1):
            k = sum(1 for p, _, _ in probs[:i] if p > 0)
            for j in range(k, -1, -1):
                if j == k:
                    dp[i][j] = dp[i-1][k] * min(p for p, _, _ in probs[i-1])
                else:
                    dp[i][j] = dp[i-1][j] * (1 - min(p for p, _, _ in probs[i-1]))
        print('%.6f' % dp[n][n])

if __name__ == '__main__':
    solve()
