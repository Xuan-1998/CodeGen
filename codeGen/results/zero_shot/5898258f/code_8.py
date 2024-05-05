def max_xor_sum(A, X):
    n = len(A)
    xor_sum = 0
    for i in range(1, n):
        xor_sum += A[i-1] ^ A[i]
    
    # Try to maximize the sum by adding X to a subsequence
    max_xor_sum = xor_sum
    for i in range(n):
        xor_sum += X if (A[i-1] if i > 0 else 0) ^ A[i] >= X else -X
        max_xor_sum = max(max_xor_sum, xor_sum)
    
    return max_xor_sum

T = int(input())  # number of test cases
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(max_xor_sum(A, X))
