import sys

def can_partition(n, k, m, arr):
    # Sort the array in non-decreasing order
    arr.sort()
    
    max_val = 0
    partitions = 1
    
    for num in arr:
        if num > max_val + M:
            max_val = num
            partitions += 1
        else:
            max_val = max(max_val, num)
        
        if partitions >= K:
            return True
    
    return False

n, k, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

print(can_partition(n, k, m, arr))
