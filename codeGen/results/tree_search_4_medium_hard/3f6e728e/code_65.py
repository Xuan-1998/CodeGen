import sys

# Pre-compute all possible pairs of upper and lower hemispheres' radii
upper_radii = []
lower_radii = []
for _ in range(N):
    u = int(input())
    upper_radii.append(u)
for _ in range(M):
    l = int(input())
    lower_radii.append(l)

dp = {}
def transition(i, j):
    if (i, j) in dp:
        return dp[(i, j)]
    if i == 0 or j == 0:
        return 1
    result = 0
    for k in range(1, i+1):
        for m in range(M+1):
            for l in range(j+1):
                if u <= c and l >= r:
                    result += (transition(k-1, j) * dp.get((m-k+1, l-1), 0)) % (10**9 + 7)
    dp[(i, j)] = result
    return result

T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    if N > M:
        N, M = M, N
    result = transition(N, M)
    print(result % (10**9 + 7))
