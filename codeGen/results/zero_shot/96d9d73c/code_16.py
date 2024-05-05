def canPartition(A):
    A.sort()
    partitions = 0
    start = 0

    for i in range(1, len(A)):
        if abs(A[i] - A[i-1]) > M:
            partitions += 1
            start = i
        elif i - start + 1 < K:
            return False

    return partitions <= N // K


N, K, M = map(int, input().split())
A = list(map(int, input().split()))

print(canPartition(A))
