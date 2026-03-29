from collections import defaultdict

def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        dp = [[0] * (C + 1) for _ in range(N + 1)]

        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == 0:
                result = C
            else:
                result = sum(dfs(k, j-1) * (U[k] >= U[i]) for k in range(i-1, -1, -1))
            memo[(i, j)] = result
            return result

        print(sum(dfs(k, C) for k in range(N)))
