import sys

def expected_carries(N):
    k = N
    E = 0.0
    for i in range(k):
        a = int(input(f"Enter digit {i+1} of A: "))
        b = int(input(f"Enter digit {i+1} of B: "))
        p = (a + b >= 10) / 10.0
        E += p
    return E

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(expected_carries(N))
