import sys

n, k, m = map(int, input().split())
arr = list(map(int, input().split()))

if sum(1 for x in arr if x >= (max(arr) + min(arr)) // 2) < k:
    print("False")
else:
    partitions = []
    partition = [arr[0]]
    max_val = partition[0]
    
    for i in range(1, n):
        if arr[i] - max_val <= m:
            partition.append(arr[i])
            max_val = max(partition)
        else:
            if len(partition) >= k:
                partitions.append(partition)
            partition = [arr[i]]
            max_val = arr[i]
    
    if len(partition) >= k:
        partitions.append(partition)
    
    for p in partitions:
        if max(p) - min(p) > m:
            print("False")
            break
    else:
        print("True")
