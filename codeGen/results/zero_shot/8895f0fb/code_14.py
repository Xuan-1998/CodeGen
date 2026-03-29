import sys

def calculate_expected_carries(N):
    # Calculate the total number of pairs
    N1 = 10 ** N
    N2 = 10 ** N
    total_pairs = N1 * N2

    # Initialize the expected number of carries
    expected_carries = 0.0

    for i in range(N):
        # Calculate the maximum value the digit could take
        max_digit = 9 - i

        # Calculate the expected number of carries for this pair
        expected_carry = (max_digit ** 2 + max_digit) / 10.0

        # Add to the total expected number of carries
        expected_carries += expected_carry

    # Return the expected number of non-zero carries per pair
    return expected_carries / total_pairs

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(calculate_expected_carries(N))
