def check_partition(N, K, M, A):
    A.sort()
    for i in range(1, N):
        if abs(A[i] - A[i-1]) > M:
            return False
    return True

print(check_partition(N, K, M, A))
