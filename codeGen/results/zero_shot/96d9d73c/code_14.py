import sys

def is_possible_partitioning():
    n, k, m = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Sort the array in non-decreasing order
    A.sort()
    
    partitions = []
    prev_end = 0
    
    for i in range(n):
        if i == 0 or A[i] - A[prev_end] > m:
            partitions.append((A[prev_end], i))
            prev_end = i
        
        if len(partitions) * (i + 1 - prev_end) >= k:
            break
    
    # Check the condition: K ≤ N
    return len(partitions) <= n // k

print(is_possible_partitioning())
