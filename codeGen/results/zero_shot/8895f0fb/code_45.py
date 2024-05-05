import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    total_carries = 0
    for i in range(10 ** (N - 1), 10 ** N):
        for j in range(i, 10 ** N):
            carries = sum((int(digit1) + int(digit2)) >= 10 for digit1, digit2 in zip(str(i)[::-1], str(j)[::-1]))
            total_carries += carries
    expected_value = total_carries / (T * (10 ** N - 1))
    print(expected_value)
