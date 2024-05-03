dp = {}
def dfs(i):
    if i >= n:
        return 1
    if (i,) in dp:
        return dp[(i,)]
    p1 = P[i] * (1 - P[i+1])
    p2 = P[i] * P[i+1]
    prob = (p1 + p2) / P[i]
    dp[(i,)] = prob
    return prob

n = int(input())
for _ in range(n):
    n, p1, p2 = map(int, input().split())
    P = [p1, p2]
    prob = 1
    for i in range(1, n+1):
        prob *= dfs(i-1)
    print(round(prob, 6))
