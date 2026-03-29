import sys

def can_partition(A):
    A.sort()
    max_val = A[-1]
    partitions = []
    
    for i, x in enumerate(A):
        if len(partitions) < K - 1:
            partitions.append([x])
        else:
            partition = min(partitions, key=lambda p: max(p))
            if abs(x - max(partition)) <= M:
                partition.append(x)
            else:
                return False
    
    return True

N, K, M = map(int, sys.stdin.readline().split())
A = [int(x) for x in sys.stdin.readline().split()]
print(can_partition(A))
