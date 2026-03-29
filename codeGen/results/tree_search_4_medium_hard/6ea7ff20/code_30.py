def can_merge(p):
    n = len(p) // 2
    a, b = set(), set()
    for i in range(n):
        if p[2*i] < p[2*i+1]:
            a.add(p[2*i])
            b.add(p[2*i+1])
        else:
            b.add(p[2*i])
            a.add(p[2*i+1])

    dp = [[False for _ in range(n+1)] for _ in range(n+1)]

    def merge(i, j):
        if i == 0 or j == 0:
            return i == 0 and not j
        if (i, j) in memo:
            return memo[(i, j)]
        if p[i+j-1] in a or p[i+j-1] in b:
            return False
        dp[i][j] = merge(i-1, j-1)
        return dp[i][j]

    memo = {}
    result = merge(n, 0)

    print("YES" if result else "NO")

# Example usage:
can_merge([1, 3, 2, 4])
