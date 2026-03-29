from collections import defaultdict

def can_partition(arr):
    N, K, M = map(int, input().split())
    dp = defaultdict(bool)
    
    for i in range(N + 1):
        if i < K:
            dp[(i, 1)] = True
        else:
            for j in range(1, min(i // K + 1, K) + 1):
                if (i - K * j >= 0 and all(abs(arr[i] - arr[m]) <= M for m in range(i - K * j, i))):
                    dp[(i, j)] = True
                elif j == 1:
                    dp[(i, j)] = any(dp[(m, j - 1)] for m in range(i - K + 1)):
    
    return dp[(N, K)]

print(can_partition(map(int, input().split())))
