import sys

def expected_non_zero_carries():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        total_carries = 0
        for i in range(2 ** N):  # iterate over all pairs of A and B
            a = i
            b = (1 << N) - 1 - i  # calculate the complement of i
            carries = 0
            carry = 0
            for j in range(N):
                digit_sum = (a // (10 ** j)) + (b // (10 ** j))
                if digit_sum >= 10:
                    carries += 1
                    carry = digit_sum % 10
                    a %= (10 ** (j + 1))
                    b %= (10 ** (j + 1))
                else:
                    a %= (10 ** (j + 1))
                    b %= (10 ** (j + 1))
            total_carries += carries
        print(total_carries / (2 ** N))

expected_non_zero_carries()
