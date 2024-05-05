import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    A, B = map(int, sys.stdin.readline().split())
    carries = 0
    for i in range(N):
        digit_sum = (A % 10 + B % 10) // 9
        if digit_sum >= 1:
            carries += 1
        A //= 10
        B //= 10
    expected_carries = carries / (N ** 2)
    print(expected_carries)
