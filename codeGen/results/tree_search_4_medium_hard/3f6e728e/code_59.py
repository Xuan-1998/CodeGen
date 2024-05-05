from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i == 0:
        return [1]
    if j == 0:
        return []
    
    result = []
    for k in range(i):
        if L_0 <= max(U_1, ..., U_k) and j > 0:
            for seq in dp(k, j-1):
                result.append(seq * sum(dp[m][j] for m in range(k)))
    return result

N, M, C = map(int, input().split())
U = list(map(int, input().split()))
L = list(map(int, input().split()))

result = []
for i in range(N+1):
    for j in range(M+1):
        if L_0 <= max(U_1, ..., U_i) and j > 0:
            result.extend(dp(i, j))
print(*result, sep=' ')
