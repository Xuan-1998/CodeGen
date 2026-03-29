import sys

T = int(input())  # Read T from stdin

for _ in range(T):
    N = int(input())  # Read N from stdin
    expected_carries = 0

    for i in range(N):
        # Calculate the sum of two digits (a, b) at position i
        a = int(input())
        b = int(input())
        carry = (a + b) // 10
        if carry:
            expected_carries += 1

    print(expected_carries / (N ** 2))  # Print the expected number of carries
