from collections import defaultdict

def canPartition(i, k, m):
    if (i, k) in memo:
        return memo[(i, k)]
    if i < 0 or k <= 0:
        return False
    if A[i-1] - A[0] > m:
        return False
    for j in range(k, 0, -1):
        if canPartition(i-j, j, m) and (j == 1 or A[i-1] - A[i-j] <= m):
            memo[(i, k)] = True
            return True
    memo[(i, k)] = False
    return False

memo = defaultdict(bool)
N, K, M = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N+1):
    for j in range(K+1):
        if canPartition(i, j, M) and (j == 1 or A[i-1] - A[0] <= M):
            print(True)
            exit(0)
print(False)
