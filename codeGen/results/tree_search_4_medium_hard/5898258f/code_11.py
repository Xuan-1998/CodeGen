def solve(N, X, A):
    memo = {0: 0}

    def dp(i):
        if i in memo:
            return memo[i]
        
        res = max(dp(i-1), A[i] ^ (A[i-1]-X))
        memo[i] = res
        return res

    res = dp(N)
    for i in range(2, N+1):
        res += A[i] ^ A[i-1]
    return max(res, X)

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, X, A))
