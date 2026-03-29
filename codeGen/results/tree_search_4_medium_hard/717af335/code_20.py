def findXY(A, B):
    memo = {}
    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == 0 and j == 0:
            return False
        if i > A or j > min(A, B):
            return True
        if i + j != A or i ^ j != B:
            return True
        memo[(i, j)] = dfs(i - 1, j) and dfs(i, j - 1)
        return not memo[(i, j)]
    for x in range(A + 1):
        y = A - x
        if dfs(x, y):
            return f"{x} {y}"
    return "-1"

A = int(input())
B = int(input())
print(findXY(A, B))
