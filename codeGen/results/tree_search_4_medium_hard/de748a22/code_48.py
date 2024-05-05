import sys

def query_sign_sum(A, l, r):
    return sum(1 if x > 0 else -1 for x in A[l:r+1])

def dp(i, j):
    if i == j:
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    sign_sum = query_sign_sum(A, i, j)
    if sign_sum == 0:
        return 0
    min_removed = float('inf')
    for k in range(i, j+1):
        removed = dp(i, k-1) + ((A[k] > 0) * 2 - sign_sum) % 2
        min_removed = min(min_removed, removed)
    memo[(i, j)] = min_removed
    return min_removed

n, q = map(int, input().split())
A = list(input())

memo = {}
min_removeds = []
for _ in range(q):
    l, r = map(int, input().split())
    min_removeds.append(dp(l, r))

print(*min_removeds, sep='\n')
