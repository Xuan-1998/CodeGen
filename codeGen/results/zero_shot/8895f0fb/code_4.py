import sys
from math import sqrt

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    total_carries = 0
    for i in range(N):
        for j in range(i+1, N):
            carry_count = sum(int(digit1) + int(digit2) >= 10 for digit1, digit2 in zip(str(i).zfill(N), str(j).zfill(N)))
            total_carries += carry_count
    expected_value = total_carries / (N ** 2)
    print(expected_value)
