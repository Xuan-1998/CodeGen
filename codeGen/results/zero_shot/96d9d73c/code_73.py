import sys

def canPartition(A):
    A.sort()
    last = A[0]
    count = 1
    for num in A:
        if abs(num - last) <= M:
            last = num
        else:
            count += 1
        if count > N // K:
            return False
    return True

N, K, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
print(canPartition(A))
