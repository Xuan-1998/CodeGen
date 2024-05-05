import sys
from collections import defaultdict

def can_partition(n, k, m, arr):
    arr.sort()
    partition_sum = 0
    partitions = 0
    
    for num in arr:
        if partition_sum + num > m:
            partition_sum = 0
            partitions += 1
        
        partition_sum += num
        
        if partitions >= k - 1:
            return True
    
    return False

if __name__ == "__main__":
    n, k, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    
    print(can_partition(n, k, m, arr))
