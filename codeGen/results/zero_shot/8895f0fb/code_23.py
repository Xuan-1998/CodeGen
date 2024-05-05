import sys
import math

def calculate_expected_carries():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        expected_carries = 0
        total_pairs = (10**N) * (10**N)
        
        for a in range(10**N):
            for b in range(10**N):
                carry_count = 0
                for i in range(N):
                    sum_digits = int(str(a // 10**i)[-1]) + int(str(b // 10**i)[-1])
                    if sum_digits >= 10:
                        carry_count += 1
                expected_carries += carry_count
        
        print(expected_carries / total_pairs)

if __name__ == "__main__":
    calculate_expected_carries()
