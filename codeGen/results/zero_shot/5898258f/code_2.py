import sys

def max_xor_sum(A, X):
    n = len(A)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] ^ A[i - 1]

    max_sum = 0
    for i in range(n // 2 + 1):
        left_sum = 0
        right_sum = 0
        for j in range(i):
            left_sum ^= A[j]
        for k in range(n - i, n):
            right_sum ^= A[k]

        max_sum = max(max_sum, abs(left_sum) + abs(right_sum))

    return max_sum

T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(max_xor_sum(A, X))
