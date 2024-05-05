import itertools

def calculate_expected_carries(N):
    # Generate all possible pairs of N-digit numbers A and B
    pairs = list(itertools.product(range(10**N), range(10**N)))

    total_carries = 0
    for pair in pairs:
        A, B = pair
        sum_digits = str(A + B)
        carries = sum(carry for digit in sum_digits if int(digit) >= 10)
        total_carries += carries

    expected_carries = total_carries / len(pairs)
    return expected_carries

# Read input from stdin and print the answer to stdout
T = int(input())
for _ in range(T):
    N = int(input())
    expected_carries = calculate_expected_carries(N)
    print(expected_carries)
