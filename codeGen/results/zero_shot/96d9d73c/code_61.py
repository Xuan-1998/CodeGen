import sys

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

for i in range(N):
    if A[i] + M >= A[K-1]:
        return "False"
    if i < N-K+1 and A[i+K-1]-A[i] > M:
        return "False"

print("True")
