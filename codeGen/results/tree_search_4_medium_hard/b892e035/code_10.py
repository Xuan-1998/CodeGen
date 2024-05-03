import sys
from collections import defaultdict

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        P = []
        A = []
        B = []
        for i in range(n):
            p, a, b = map(int, input().split())
            P.append(p)
            A.append(a)
            B.append(b)

        dp = [[0.0 for _ in range(3)] for _ in range(n+1)]
        dp[0][0] = 1.0

        for i in range(1, n+1):
            p, a, b = P[i-1], A[i-1], B[i-1]
            if a == b:
                dp[i][2] = (p*a + (1-p)*b) * dp[i-1][2]
            elif a != b:
                dp[i][0] = (p*a + (1-p)*b) * dp[i-1][0]
                dp[i][1] = (p*a + (1-p)*b) * dp[i-1][1]

        print(dp[n][0])

if __name__ == "__main__":
    solve()
