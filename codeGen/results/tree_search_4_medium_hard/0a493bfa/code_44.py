def max_beauty(n, m, bad_primes):
    memo = {}
    
    def beauty(i, last):
        if (i, last) in memo:
            return memo[(i, last)]
        
        if i == 0:
            return 0
        
        total = 0
        for j in range(i):
            if a[j] not in bad_primes and gcd(a[i-1], a[j]) != a[i-1]:
                total += beauty(j, a[i-1])
        
        return max(total, last + a[i-1])
    
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bad_primes = set(map(int, input().split()))

    for i in range(1, n):
        memo[(i, a[i-1])] = beauty(i, 0)
    
    return max(memo.values())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, m = map(int, input().split())
a = list(map(int, input().split()))
bad_primes = set(map(int, input().split()))

print(max_beauty(n, m, bad_primes))
