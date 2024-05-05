import sys

n, k, m = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = True
curr_partition = [A[0]]
for i in range(1, n):
    if abs(A[i] - curr_partition[-1]) <= m:
        curr_partition.append(A[i])
    else:
        if len(curr_partition) < k:
            ans = False
            break
        curr_partition = [A[i]]

print(ans)
