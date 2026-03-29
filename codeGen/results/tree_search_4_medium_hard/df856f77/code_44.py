def min_operations(A):
    N = len(A)
    memo = [[0] * N for _ in range(N)]

    def dfs(i, j):
        if i == j:
            return 0
        if memo[i][j]:
            return memo[i][j]

        if A[i] <= A[j]:
            # Include Ai in the increasing subsequence
            return dfs(i + 1, j) + (A[i] - A[i - 1]) if i > 0 else 0
        else:
            # Start a new increasing subsequence from this point
            return 1 + min(dfs(i + 1, j), dfs(i, j - 1))

    return dfs(0, N - 1)

N = int(input())
A = list(map(int, input().split()))
print(min_operations(A))
