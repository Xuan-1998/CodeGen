import sys

N, K, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

A.sort()

min_val = A[0]
max_val = A[0]

for i in range(N):
    min_val = min(min_val, A[i])
    max_val = max(max_val, A[i])

    if max_val - min_val > M:
        print(False)
        sys.exit(0)

if (A.index(A[K-1]) < N-K+1) and ((max_val - min_val <= M)):
    print(True)
else:
    print(False)
