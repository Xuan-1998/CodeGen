import sys

n, k, m = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

start = 0
max_val = A[0]
end = 0
for i in range(1, n):
    if A[i] - max_val > m:
        start = end + 1
        max_val = A[i]
    else:
        end += 1

if end / k >= start and end % k == 0:
    print(True)
else:
    print(False)
