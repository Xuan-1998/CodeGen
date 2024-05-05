import sys
from collections import defaultdict

def expected_carries(T):
    total_pairs = 0
    total_carries = 0

    for _ in range(T):
        N = int(sys.stdin.readline())
        total_pairs += (10**N - 1)**2

        for i in range(1, 11**N):
            a = [int(x) for x in str(i)]
            carries = sum(1 for j in range(N-1) if int(str(a[j] + a[-1 -j]).lstrip('0') or ''))
            total_carries += carries

    return total_carries / total_pairs

T = int(sys.stdin.readline())
print(expected_carries(T))
