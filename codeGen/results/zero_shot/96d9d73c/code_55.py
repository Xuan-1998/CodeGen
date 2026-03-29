import sys

N, K, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.read().split()))

if A[K-1] - A[0] > M:
    print(False)
else:
    print(True)
