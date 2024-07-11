MOD = 998244353
N = int(input().strip())
D = list(map(int, input().strip().split()))

if D[0] != 1:
    print(0)
else:
    count = [0]*N
    count[0] = 1
    sum_count = [0]*(N+1)
    sum_count[1] = 1
    p = [0]*N
    for i in range(1, N):
        p[i] = sum_count[D[i]]
        sum_count[D[i]+1] += p[i]
        sum_count[D[i]+1] %= MOD
    ans = 1
    for i in range(N-1, -1, -1):
        ans *= p[i]
        ans %= MOD
    print(ans)

