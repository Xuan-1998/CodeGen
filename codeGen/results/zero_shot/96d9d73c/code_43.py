def can_partition(A):
    A.sort()
    partitions = []
    curr_partition = [A[0]]
    
    for i in range(1, len(A)):
        if abs(A[i] - curr_partition[-1]) <= 10**9:
            curr_partition.append(A[i])
        else:
            if len(curr_partition) >= K:
                partitions.append(curr_partition)
            else:
                return False
            curr_partition = [A[i]]
    
    if len(curr_partition) >= K:
        partitions.append(curr_partition)
    else:
        return False
    
    return True

N, K, M = map(int, input().split())
A = list(map(int, input().split()))
print(can_partition(A))
