def find_XY(A, B):
    memo = {}

    def dp(x):
        if x > min(A, B):
            return float('inf')
        y = A - x
        if B == x ^ y:
            return 0
        if (x, y) in memo:
            return memo[(x, y)]
        res = 1 + dp(x + 1)
        memo[(x, y)] = res
        return res

    min_res = float('inf')
    for x in range(min(A, B) + 1):
        if dp(x) < min_res:
            min_res = dp(x)

    if min_res == float('inf'):
        return -1
    else:
        X = min_res
        Y = A - X
        return f"{X} {Y}"

A, B = map(int, input().split())
print(find_XY(A, B))
