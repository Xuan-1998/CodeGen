def can_partition(A, K, M):
    A.sort()
    
    partitions = 0
    current_bucket = [A[0]]
    
    for num in A[1:]:
        if len(current_bucket) >= K or abs(num - current_bucket[-1]) > M:
            partitions += 1
            current_bucket = [num]
        else:
            current_bucket.append(num)
    
    return partitions + (len(current_bucket) < K)

# Example usage:
N, K, M = map(int, input().split())
A = list(map(int, input().split()))
print(can_partition(A, K, M))
