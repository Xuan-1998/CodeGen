def steady_tables(N, M):
    MOD = 10**9 + 7
    ans = 0
    for k in range(M+1):
        ans += math.comb(N-1, k) % MOD
    return ans

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(steady_tables(N, M))
