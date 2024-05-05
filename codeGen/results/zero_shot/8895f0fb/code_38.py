import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    total_carry = sum((N-i) * (9 - i) for i in range(N))
    print(total_carry / (N * 10), end=' ')
