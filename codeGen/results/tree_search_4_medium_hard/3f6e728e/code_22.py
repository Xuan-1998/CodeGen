import math

T = int(input())
for t in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    dp = [0]*(C+1)
    dp[1] = 1

    for i in range(C):
        C_count = [0]*C
        for j in range(N+M):
            if U[j] <= i:
                C_count[U[j]-1] += 1
            if L[j] <= i:
                C_index = 1
            else:
                C_index = 2
            C_count[C_index-1] += 1

        for j in range(1, i+1):
            dp[i+1] += (dp[j]*math.comb(C_count[C_index-1].get(j, 0), C_count[C_index-1].get(j, 0))) % (10**9 + 7)

    print(*[str(dp[i]) for i in range(2, C+1)], sep=' ')
