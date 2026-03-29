import sys
from itertools import product

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    
    total_carries = 0
    for a, b in product(range(10**N), range(10**N)):
        carry_count = sum((int(d1) + int(d2)) >= 10 for d1, d2 in zip(str(a)[::-1], str(b)[::-1])))
        total_carries += carry_count
    
    expected_carries = total_carries / (10**N)**2
    print('%.6f' % expected_carries)
