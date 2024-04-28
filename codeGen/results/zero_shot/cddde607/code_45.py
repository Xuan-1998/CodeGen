def count_paths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]
    dp[0][0][0] = 1
    for i in range(1, N):
        for j in range(N):
            if i == 0:
                dp[i][j][0] = 1
            else:
                for k in range(min(K, arr[i][j])):
                    dp[i][j][k+1] += dp[i-1][j][k]
    result = 0
    for j in range(N):
        if N - 1 == j:
            result += dp[N-1][j][K]
        else:
            for k in range(K + 1):
                result += dp[N-1][j+1][k]
    return result

import sys
read = lambda: map(int, sys.stdin.readline().split())
write = lambda x: sys.stdout.write(str(x) + '\n')
write(count_paths(*read()))
