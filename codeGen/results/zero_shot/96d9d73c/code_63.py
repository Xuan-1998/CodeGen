import sys

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

low, high = 1, A[-1]

while low <= high:
    mid = (low + high) // 2
    if len([x for x in A if x - mid >= 0 and x - mid < M]) >= K:
        low = mid + 1
    else:
        high = mid - 1

if any(A[i] - A[i-1] > M for i in range(1, N)):
    print(False)
else:
    print(low >= M)
