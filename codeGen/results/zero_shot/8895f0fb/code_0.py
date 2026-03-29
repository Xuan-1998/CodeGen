import sys

def calculate_expected_carries(t):
    n = int(sys.stdin.readline().strip())
    total_pairs = 1
    for _ in range(n):
        total_pairs *= (10**_ + 1)
    
    total_carries = 0
    for i in range(1, n+1):
        for j in range(i):
            a = int('9' * i)
            b = int('9' * j) - 1 if j > 0 else 0
            carries = sum((int(str(a)) + int(str(b))) >= 10)
            total_carries += carries
    
    expected_carries = total_carries / total_pairs
    return "{:.6f}".format(expected_carries)

t = int(sys.stdin.readline().strip())
for _ in range(t):
    print(calculate_expected_carries(1))
