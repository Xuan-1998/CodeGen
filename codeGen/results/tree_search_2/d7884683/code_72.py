from collections import defaultdict

def max_partition(n, arr):
    total_sum = sum(arr)
    dp = {(i, 0, n) for i in range(n+1)}

    for i in range(1, n+1):
        left_sum = 0
        for j in range(i-1, -1, -1):
            left_sum += arr[j]
            if (j, left_sum, i) in dp:
                dp[(i, left_sum, i)] = max(dp.get((i, left_sum, i), 0), dp.get((j, 0, i), 0) + 1)

    max_count = 0
    for k, v in dp.items():
        if k[2] == n:
            max_count = max(max_count, v)
    return max_count

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partition(n, arr))
