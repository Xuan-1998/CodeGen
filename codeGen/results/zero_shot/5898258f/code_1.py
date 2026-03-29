def max_xor_sum(A, X):
    n = len(A)
    prefix_xor = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_xor[i] = prefix_xor[i-1] ^ A[i-1]

    max_sum = 0
    for i in range(2, n + 1):
        max_sum = max(max_sum, prefix_xor[i - 1] ^ A[i])

    return max_sum

t = int(input())
for _ in range(t):
    n, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(max_xor_sum(A, X))
