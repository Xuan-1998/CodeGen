def mergeable(p):
    n = len(p) // 2
    dp = {}

    def dfs(i, j):
        if (i, j) in dp:
            return dp[(i, j)]

        if j == 0:  # Base case: a is empty
            b = p[i:]
            return b == sorted(b)

        if p[i] > p[0]:
            a = [p[0]]
            for k in range(1, i):
                a.append(p[k])
            b = p[i:]
            result = dfs(i - 1, j - 1)
            if not result:
                return False
            return True

        a = p[:i]
        b = p[i:]
        result = dfs(i, j - 1)
        if not result:
            return False
        return True

    for i in range(n):
        if not dfs(n - 1, n - i - 1):
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(mergeable(p))
