def max_xor_sum(A, X):
    N = len(A)
    max_sum = 0
    current_sum = 0

    for i in range(2, N // 2 + 1):
        sum_xor = A[i-1] ^ A[i]
        current_sum += sum_xor
        if i % 2 == 0:
            current_sum += X
        else:
            current_sum -= X
        max_sum = max(max_sum, current_sum)

    for i in range(N // 2 + 1, N):
        sum_xor = A[i-1] ^ A[i]
        current_sum -= sum_xor
        if i % 2 == 0:
            current_sum += X
        else:
            current_sum -= X
        max_sum = max(max_sum, current_sum)

    return max_sum

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(max_xor_sum(A, X))
