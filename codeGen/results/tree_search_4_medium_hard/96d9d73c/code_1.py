from sys import stdin

def can_partition(n, k, m):
    dp = [[False for _ in range(k)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True

    for i in range(1, n+1):
        for j in range(1, min(i, (n-1)//k)+1):
            if dp[i-1][min(j, (i-1)//k)]:
                dp[i][j] = True
            else:
                dp[i][j] = False

    return dp[n][k-1]

n, k, m = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
print(can_partition(n, k, m))
