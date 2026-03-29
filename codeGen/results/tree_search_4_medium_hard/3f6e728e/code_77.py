import math

def choose(n, k):
    if k > n // 2:
        k = n - k
    result = 1
    for i in range(k):
        result = (result * (n - i)) // (i + 1)
    return result

def solve():
    T = int(input())
    memo = {}
    
    def dp(N, M, C):
        if (N, M) in memo:
            return memo[(N, M)]
        
        if N == 0 or M == 0:
            return 1
        
        result = 0
        for i in range(C + 1):
            if i <= N and i <= M:
                result += math.prod(choose(N, i), dp(M - i, N - i, C)) % (10**9 + 7)
        
        memo[(N, M)] = result
        return result
    
    for _ in range(T):
        N, M, C = map(int, input().split())
        print(dp(N, M, C) % (10**9 + 7))

solve()
