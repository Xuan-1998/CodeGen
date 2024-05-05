import sys

def expected_non_zero_carries(T, N):
    total_pairs = 10 ** (N * 2)  # calculate total number of pairs
    total_carry_count = 0  # initialize carry count for all pairs

    for _ in range(T):  # iterate over test cases
        A = int(input())  # read input A
        B = int(input())  # read input B

        carry_count = 0  # initialize carry count for this pair

        # calculate non-zero carries when adding A and B
        while len(str(A)) > 0 and len(str(B)) > 0:
            if (A % 10 + B % 10) >= 10:  # check for carry
                carry_count += 1
            A //= 10
            B //= 10

        total_carry_count += carry_count  # add to overall carry count

    return total_carry_count / total_pairs  # calculate and return expected value

T = int(sys.stdin.readline())  # read number of test cases

for _ in range(T):
    N = int(sys.stdin.readline())  # read maximum number of digits
    print(expected_non_zero_carries(1, N))  # calculate and print expected value for this test case
