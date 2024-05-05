import sys

def calculate_expected_carry(n):
    total_pairs = n ** 2
    carry_count = 0
    
    for i in range(1, 10):  # iterate through each digit from 1 to 9
        for j in range(1, 10):  # iterate through each digit from 1 to 9
            sum_of_digits = i + j
            if sum_of_digits >= 10:  # check if the sum is greater than or equal to 10
                carry_count += 1
    
    expected_carry = carry_count / total_pairs
    return expected_carry

T = int(sys.stdin.readline())  # read the number of test cases
for _ in range(T):
    N = int(sys.stdin.readline())  # read the maximum number of digits in A and B
    print(calculate_expected_carry(N))  # calculate and print the expected number of non-zero carries
