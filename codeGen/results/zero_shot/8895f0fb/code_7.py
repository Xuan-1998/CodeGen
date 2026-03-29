import sys

def expected_carries():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        total_pairs = 10 ** (N - 1)
        
        expected_carries = 0
        
        for _ in range(total_pairs):
            a, b = map(int, str(9 * 10 ** (N - 1) + 10 ** (N - 1)).zfill(N))
            carry_count = sum((a // 10 ** i) % 10 + (b // 10 ** i) % 10 >= 10 for i in range(N))
            expected_carries += carry_count
        
        print(expected_carries / total_pairs)

expected_carries()
