import sys

def expected_carries(n):
    total_pairs = 10 ** n
    carries_per_pair = 0
    
    # Iterate over all possible digit values (0-9)
    for i in range(10):
        for j in range(i, 10):
            # Check if the sum of two digits results in a value greater than or equal to 10
            if i + j >= 10:
                carries_per_pair += 1
    
    return carries_per_pair / total_pairs

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(expected_carries(n))
