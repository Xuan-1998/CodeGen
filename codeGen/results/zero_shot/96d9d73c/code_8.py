# Read input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

def can_partition():
    A.sort()
    left, right = 0, N - 1
    while left < right:
        if A[right] - A[left] > M:
            return False
        left += 1
        right -= 1
    for i in range(N - K + 1):
        if A[i + K - 1] - A[i] > M:
            return False
    return True

print(can_partition())
