t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    prefix_sum = [0]
    for x in arr:
        prefix_sum.append(prefix_sum[-1] + x)
    
    max_partitions = 0
    left_sum = prefix_sum[0]
    right_sum = sum(arr) - left_sum
    partitions = 0
    
    while True:
        if left_sum == right_sum:
            partitions += 1
            max_partitions = max(max_partitions, partitions)
            left_sum = prefix_sum[partitions * 2 + 1]
            right_sum = sum(arr[:partitions * 2 + 1]) - left_sum
        elif left_sum < right_sum:
            left_sum += prefix_sum[-1] - prefix_sum[partitions * 2 + 1]
        else:
            right_sum -= prefix_sum[partitions * 2 + 1] - prefix_sum[partitions * 2]
        
        if partitions >= n // 2:
            break
    print(max_partitions)
