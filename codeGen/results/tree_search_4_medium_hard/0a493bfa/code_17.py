import heapq
from collections import defaultdict

def good_prime(n):
    primes = []
    for i in range(2, n+1):
        if all(i%j>0 for j in range(2,int(i**0.5)+1)):
            primes.append(i)
    return primes

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = good_prime(max(b))

    dp = defaultdict(int)
    pq = [(0, 0)]

    while pq:
        cur_beauty, i = heapq.heappop(pq)
        if i >= n:
            return cur_beauty
        for j in range(m):
            k = min(i+1, len(a))
            g = a[i]
            for p in range(k-1, -1, -1):
                while b[j] > 0 and a[p]%b[j]==0:
                    b[j] //= a[p]
                    p -= 1
                if all(a[p]%b[j]>0 for p in range(k)):
                    break
            g = max(g, a[i])
            if i+1 < n:
                heapq.heappush(pq, (cur_beauty + g, i+1))
    return -1

print(solve())
