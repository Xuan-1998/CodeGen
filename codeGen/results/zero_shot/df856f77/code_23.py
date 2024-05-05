import sys

N = int(input())
A = list(map(int, input().split()))

operations = 0
for i in range(1, N):
    if A[i] <= A[i-1]:
        diff = A[i-1] - A[i] + 1
        operations += diff
        A[i] += diff

print(operations)
