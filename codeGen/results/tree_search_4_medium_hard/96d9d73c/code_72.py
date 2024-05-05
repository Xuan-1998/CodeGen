import sys

def can_partition(A):
    N, K, M = map(int, input().split())
    dp = [[False for _ in range(K+1)] for _ in range(N+1)]

    for i in range(N+1):
        for j in range(1, min(i, K)+1):
            if i < K:
                dp[i][j] = False
            else:
                for p in range(j-1, i+1):
                    if all(abs(A[p]-A[q]) <= M for q in range(p)):
                        if p >= K and j > 1 and dp[p-K][j-1]:
                            dp[i][j] = True
                            break

    return dp[N][K]

print(can_partition(list(map(int, input().split()))))
