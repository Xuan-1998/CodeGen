def mergeable(p):
    n = len(p) // 2
    a, b = set(), set()

    for i in range(n):
        if p[i] < p[n + i]:
            a.add(p[i])
        else:
            b.add(p[i])

    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == n and j == n:
            return False

        if i < n and j < n:
            if p[i] <= p[j]:
                memo[(i, j)] = dp(i + 1, j)
            else:
                memo[(i, j)] = dp(i, j + 1)

        elif i < n:
            memo[(i, j)] = True

        elif j < n:
            memo[(i, j)] = True

        return not memo[(i, j)]

    if dp(0, 0):
        return "YES"
    else:
        return "NO"

# Read input from standard input
n = int(input())
p = list(map(int, input().split()))

print(mergeable(p))
