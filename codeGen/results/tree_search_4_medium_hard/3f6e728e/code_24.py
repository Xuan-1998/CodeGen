memo = {}
def dfs(i):
    if i in memo:
        return memo[i]
    if i > C:
        return 1
    if i < 0:
        return 0
    res = 0
    for j in range(U):
        if upper[j] <= i and lower[L-1-j] >= i:
            res += dfs(i - upper[j])
    memo[i] = res % (10**9 + 7)
    return res

result = []
for _ in range(int(input())):
    N, M, C = map(int, input().split())
    U = N
    L = M
    upper = list(map(int, input().split()))
    lower = list(map(int, input().split()))
    print(*[int(dfs(i)) for i in range(C)], sep=' ')
