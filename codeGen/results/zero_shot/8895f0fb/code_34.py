import sys

def expected_carries(T, N):
    carry_count = 0
    total_pairs = N * (N + 1) // 2

    for _ in range(T):
        A = int(input())
        B = int(input())

        # Convert to binary and count carries
        a_bin = bin(A)[2:]
        b_bin = bin(B)[2:]

        # Find the maximum length of the two binary strings
        max_len = max(len(a_bin), len(b_bin))

        for i in range(max_len):
            if (a_bin[-1 - i] == '1' and b_bin[-1 - i] == '1'):
                carry_count += 1

    return carry_count / total_pairs

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(expected_carries(1, N))
