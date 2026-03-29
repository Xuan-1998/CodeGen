def can_partition(arr):
    arr.sort()
    max_diff = arr[-1] - arr[0]
    
    for i in range(len(arr) - K + 1):
        partition_sum = sum(arr[i:i+K])
        
        if max_diff <= partition_sum:
            return True
    
    return False

N, K, M = map(int, input().split())
arr = list(map(int, input().split()))
print(can_partition(arr))
