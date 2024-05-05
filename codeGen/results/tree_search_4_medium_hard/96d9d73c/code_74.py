import sys

def solve(N, K, M, A):
    memo = {}
    def dp(i, j):
        if (i, len(memo)) in memo:
            return memo[(i, len(memo))]
        res = False
        for p in range(i):
            if all(abs(x - y) <= M for x, y in zip(A[:p+1], A[0])):
                if dp(i-p-1, K-M):
                    res = True
                    break
        memo[(i, len(memo))] = res
        return res

    if any(x > M * (K - 1) for x in A):
        return False
    return dp(N, K)

N, K, M = map(int, input().split())
A = list(map(int, input().split()))
print(solve(N, K, M, A))
