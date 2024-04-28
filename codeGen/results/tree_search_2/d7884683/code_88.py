def max_partitions(arr):
    n = len(arr)
    dp = {(i, 0): i for i in range(n)}
    
    for left_sum in range(sum(arr) // 2 + 1):
        for left_len in range(1, n):
            if left_sum <= left_len and (left_len, left_sum - left_len) in dp:
                dp[(left_len, left_sum)] = max(dp.get((left_len, left_sum), 0), dp[(left_len-1, left_sum-left_len)] + 1)
    
    return max(max_partitions([arr[i] for i in range(left, n)]) for (left, _) in dp.keys())

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
