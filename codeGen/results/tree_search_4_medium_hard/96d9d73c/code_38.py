def can_partition(N, K, M, A):
    memo1 = {}
    memo2 = {}

    def dfs(i, j):
        if (i, j) in memo1:
            return memo1[(i, j)]
        if i < 0 or j <= 0:
            return True

        res = False
        for k in range(1, min(i // K + 1, M) + 1):
            if (i - k * K, k) not in memo1:
                memo1[(i - k * K, k)] = dfs(i - k * K, k)
            if memo1[(i - k * K, k)] and (k == 1 or memo2[(i - k * K, k - 1, max(M, A[i] - A[i - k * K]))]):
                res = True
                break

        memo1[(i, j)] = res
        return res

    def dfs2(i, k, m):
        if (i, k, m) in memo2:
            return memo2[(i, k, m)]
        if i < K or A[i] - A[i-K+1] > M:
            return False
        for j in range(1, min(i // K + 1, m) + 1):
            if (i-j*K, j) not in memo1:
                memo1[(i-j*K, j)] = dfs(i-j*K, j)
            if (j*K, 1) not in memo1:
                memo1[(j*K, 1)] = dfs(j*K, 1)
            if memo1[(i-j*K, j)] and memo2[(i-j*K, k-1, max(m, A[i] - A[i-j*K]))] and memo1[(j*K, 1)]:
                return True
        return False

    return dfs2(N, K, M)

N, K, M = map(int, input().split())
A = list(map(int, input().split()))
print(can_partition(N, K, M, A))
