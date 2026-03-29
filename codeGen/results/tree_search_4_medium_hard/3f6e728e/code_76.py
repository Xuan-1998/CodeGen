def count_x_sequences(N, M, C):
    dp = {0: 1}
    memo = {}

    def dfs(n, m, c):
        if (n, m, c) in memo:
            return memo[(n, m, c)]
        
        res = 0
        for i in range(c, -1, -1):
            if n < M and L[M-1-i] >= i:
                break
            
            count = dfs(n-1, m-1, i) * (N - n)
            res += count % (10**9 + 7)

        memo[(n, m, c)] = res
        return res

    return dfs(N, M, C)


# Read input from stdin
T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    print(count_x_sequences(N, M, C))
