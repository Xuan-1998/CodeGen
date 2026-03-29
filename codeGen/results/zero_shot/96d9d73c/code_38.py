N, K, M = map(int, input().split())
A = list(map(int, input().split()))
partition_possible = True
start = 0
for i in range(N):
    if (A[i] - M) > start or (A[i] + M) < end:
        partition_possible = False
        break
    if i >= K:
        start = A[i-K+1]
        end = A[i]
print(partition_possible)
