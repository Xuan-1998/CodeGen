import sys

def calculate_expected_carries(T):
    result = 0
    for _ in range(T):
        N = int(input())
        total_pairs = N * (N + 1) // 2
        carries_per_pair = 0
        for i in range(N):
            for j in range(i+1, N):
                a_digit = int(str(A)[i])
                b_digit = int(str(B)[j])
                carry = max(a_digit, b_digit) - min(a_digit, b_digit)
                if carry >= 10:
                    carries_per_pair += 1
        expected_carries = carries_per_pair / total_pairs
        result += expected_carries
    return result

T = int(input())
print(calculate_expected_carries(T))
