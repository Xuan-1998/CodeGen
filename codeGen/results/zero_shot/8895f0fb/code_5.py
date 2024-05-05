import sys

def expected_carries():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        total_carries = 0
        total_pairs = 10**2*N
        for a in range(10**N):
            for b in range(10**N):
                carries = 0
                carry = 0
                for i in range(N):
                    digit_a = (a // 10**i) % 10
                    digit_b = (b // 10**i) % 10
                    sum_digit = digit_a + digit_b + carry
                    if sum_digit >= 10:
                        carries += 1
                        carry = 1
                    else:
                        carry = 0
                total_carries += carries
        expected_value = total_carries / total_pairs
        print("{:.6f}".format(expected_value))

expected_carries()
