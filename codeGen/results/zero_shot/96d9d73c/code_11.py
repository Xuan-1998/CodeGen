current_partition = [A[0]]
for i in range(1, len(A)):
    if A[i] - current_partition[-1] > M:
        current_partition = [A[i]]
    else:
        current_partition.append(A[i])

print(len(current_partition) >= K)
