import sys

def expected_carries(n):
    # Initialize variables
    no_carry_cases = 1
    one_carry_cases = n - 1
    multiple_carry_cases = (n - 2) * (n - 3) // 2
    total_pairs = (10 ** n) ** 2

    # Calculate the expected number of carries
    expected_carries = (no_carry_cases + one_carry_cases + multiple_carry_cases * 1.5) / total_pairs

    return expected_carries

# Read input from stdin
T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    print(expected_carries(n))
