import math

def calculate_expected_carries():
    T = int(input())  # Read the number of test cases
    for _ in range(T):
        N = int(input())  # Read the maximum number of digits in A and B
        total_pairs = math.comb(10**N + 1, 2)  # Calculate the total number of pairs
        total_carries = 0  # Initialize the sum of non-zero carries
        for _ in range(total_pairs):
            a = int(input())  # Read the first N-digit number
            b = int(input())  # Read the second N-digit number
            carry_count = 0  # Initialize the count of non-zero carries for this pair
            for digit_a, digit_b in zip(str(a)[::-1], str(b)[::-1]):
                total = int(digit_a) + int(digit_b)
                if total >= 10:
                    carry_count += 1
            total_carries += carry_count  # Add the non-zero carries to the total count
        expected_carries = total_carries / total_pairs  # Calculate the expected value
        print(expected_carries)  # Print the result

calculate_expected_carries()
