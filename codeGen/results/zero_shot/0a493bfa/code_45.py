import heapq
from math import gcd

def calculate_beauty(a):
    beauty = 0
    for num in a:
        p = next((p for p in range(2, int(num**0.5) + 1) if num % p == 0), None)
        if p not in bad_primes:
            beauty += num
        else:
            beauty -= num
    return beauty

n, m = map(int, input().split())
a = list(map(int, input().split()))
bad_primes = set(map(int, input().split()))

a.sort(reverse=True)

heap = [0]
for num in a:
    while heap[0] < num:
        heapq.heappop(heap)
    beauty = 0
    for num_gcd in heap:
        g = gcd(num_gcd, num)
        if g > 1:
            beauty += g
    print(beauty)
