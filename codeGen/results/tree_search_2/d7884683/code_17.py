import sys

def count_partitions(arr):
    n = len(arr)
    dp = [False] * (n + 1)

    for i in range(n + 1):
        if i == 0 or i == 1:
            dp[i] = True
        else:
            for k in range(i):
                if arr[:k+1].sum() == arr[k+1:].sum():
                    dp[i] = True
                    break

    max_partitions = 0
    for i in range(n, -1, -1):
        if dp[i]:
            max_partitions += 1
            while dp[i-1]:
                i -= 1
    return max_partitions

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_partitions(arr))
