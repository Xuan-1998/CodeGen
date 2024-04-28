from collections import defaultdict

def max_partitions(arr):
    n = len(arr)
    dp = [False] * (n + 1)
    dp[0] = True

    memo = defaultdict(set)

    for i in range(1, n):
        for k in range(i):
            if arr[k+1:i+1].index(sum(arr[:k+1])) == -1:
                break
            if sum(arr[:k+1]) == sum(arr[k+1:]):
                dp[i] = True

    return len([i for i in range(n) if dp[i]])

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
