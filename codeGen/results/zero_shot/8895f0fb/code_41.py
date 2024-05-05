import sys

def calculate_expected_carry(T):
    # Initialize variables
    N = int(input())
    expected_carry_count = 0

    # Iterate over all possible pairs of A and B
    for i in range(N, 0, -1):
        for j in range(10**i - 1, 10**(i-1)):
            a = int(str(j) + "0" * (i-1))
            b = int(str(j+1) + "0" * (i-1))

            # Add A and B, count non-zero carries
            carry_count = 0
            while a or b:
                sum_digit = (a % 10) + (b % 10)
                if sum_digit >= 10:
                    carry_count += 1
                a //= 10
                b //= 10

            # Update expected_carry_count
            expected_carry_count += carry_count

    return expected_cary_count / (T * N ** 2)

# Read the number of test cases from stdin
T = int(sys.stdin.readline())

# Calculate and print the expected number of carries for each test case
for _ in range(T):
    result = calculate_expected_carry(1)
    print(result, end=" ")
