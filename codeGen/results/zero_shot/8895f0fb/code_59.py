import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    expected_carries = 0
    
    # Calculate the probability of non-zero carry for each column
    for _ in range(N-1):
        expected_carries += 1 / (10 ** (N - 1))
    
    print(expected_carries)
