import sys

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        A = []
        B = []
        P = []
        for _ in range(n):
            a, b, p = map(int, input().split())
            A.append(a)
            B.append(b)
            P.append(p)
        
        dp = [[0.0] * (1 << 16) for _ in range(n+1)]
        dp[0][0] = 1
        
        for i in range(1, n+1):
            p_sum = 0
            for j in range((1 << 16) - 1, -1, -1):
                if (j & (1 << A[i-1])) and (j & (1 << B[i-1])):
                    p_sum += P[i-1] / 100.0 * P[i-1] / 100.0
            for j in range((1 << 16) - 1, -1, -1):
                if dp[i-1][j]:
                    dp[i][j] = p_sum / ((2**16 - 1 - j + 1) * (i-1))
        
        print('%.6f' % dp[n][-1])

if __name__ == "__main__":
    solve()
