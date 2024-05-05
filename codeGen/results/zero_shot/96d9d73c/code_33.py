N, K, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

current_partition = [A[0]]

for i in range(1, N):
    if abs(A[i] - current_partition[-1]) <= M:
        current_partition.append(A[i])
    else:
        if len(current_partition) < K:
            print("false")
            exit()
        
        current_partition = [A[i]]

if len(current_partition) >= K:
    print("true")
else:
    print("false")
