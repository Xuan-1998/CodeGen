import sys

def count_carries(n):
    total_pairs = 10**n * 10**n
    total_non_zero_carries = 0
    
    for i in range(10**n):
        a = str(i).zfill(n)
        for j in range(10**n):
            b = str(j).zfill(n)
            sum_ab = int(a) + int(b)
            carries = sum(map(int, str(sum_ab))) - sum_ab
            total_non_zero_carries += carries
    
    return total_non_zero_carries / (total_pairs * 1.0)

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(count_carries(n))
