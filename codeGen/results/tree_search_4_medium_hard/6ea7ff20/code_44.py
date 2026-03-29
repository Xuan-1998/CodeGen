system

    system
    dp = {(i, j): 0 for i in range(2*1003) for j in range(2*1003)}
    def is_valid(i, j):
        if p[i] > p[j]:
            return dp[i][j+1] or (p[i] not in p[:j])
        elif p[i] < p[j]:
            return dp[i+1][j] or (p[i] not in p[j+1:])
        else:
            return True
    def merge(p, i):
        if i == 0:
            return []
        if p[i-1] > p[i]:
            return [p[i]] + merge(p, i-1)
        elif p[i-1] < p[i]:
            return merge(p, i-1) + [p[i]]
        else:
            return [p[i]] + merge(p, i-1)
    def solve(n, p):
        for i in range(2*n):
            if p[i] > 0:
                return "NO"
        for i in range(n):
            for j in range(i+1, n):
                if not is_valid(i, j):
                    return "NO"
        return "YES"
    for _ in range(int(input())):
        n = int(input())
        p = list(map(int, input().split()))
        print(solve(n, p))

