def can_partition(A):
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    memo = {}
    dp1 = [False] * (N + 1)
    dp2 = [False] * (N + 1)

    for i in range(N):
        if A[i] - M >= K:
            dp1[i+1] = True
            canBePartitioned = {A[i]}
            for j in range(i-1, -1, -1):
                if A[j] - M >= K and abs(A[j] - A[i]) <= M:
                    canBePartitioned.add(A[j])
                    if len(canBePartitioned) >= K:
                        dp2[i+1] = True
                        break

    return memo[(N, K)]
