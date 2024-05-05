import sys

def solution():
    T = int(input())
    for _ in range(T):
        N, X = map(int, input().split())
        A = list(map(int, input().split()))
        
        dp = [[0] * (N+1) for _ in range(N+1)]
        
        for i in range(1, N+1):
            for j in range(i, 0, -1):
                if j == i:
                    dp[i][j] = A[0]
                elif j == 1:
                    dp[i][j] = xor(A[i-1], A[i])
                else:
                    dp[i][j] = max(dp[i-1][k] + xor(A[i-1], A[k]) for k in range(j, i))
        
        print(max(dp[N][i] for i in range(N+1)))

def xor(a, b):
    return a ^ b

solution()
