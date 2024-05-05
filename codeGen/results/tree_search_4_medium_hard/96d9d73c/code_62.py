import sys

def can_partition(n, k, m, arr):
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(min(i // k, k), -1, -1):
            if all(abs(x - y) <= m for x in arr[:i]):
                dp[i][j] = True
                if i >= j * k:
                    for p in range(j * k, i):
                        if not can_partition(p, j - 1, m, arr[p:]):
                            break
                    else:
                        return True
    
    return dp[n][k]

n, k, m = map(int, input().split())
arr = list(map(int, input().split()))
print(can_partition(n, k, m, arr))
