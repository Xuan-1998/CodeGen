t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    prefix_sum = [0]
    for num in arr:
        prefix_sum.append(prefix_sum[-1] + num)
    
    max_partitions = 0
    left_sum = 0
    for i in range(1, len(prefix_sum)):
        if prefix_sum[i] - left_sum == left_sum:
            max_partitions += 1
            left_sum = 0
        else:
            left_sum = prefix_sum[i]
    
    print(max_partitions)
