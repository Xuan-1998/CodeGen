import sys

def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize all entries as true.
    prime = [True] * (n + 1)
    p = 2
    
    while (p * p <= n):
        if (prime[p]): 
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    bad_primes = [i for i in range(2, n) if prime[i]]
    
    memo = {}
    def beauty(i, j, f, b):
        if (j - i < 3):
            return 0
        
        if ((i, j, f, b) in memo):
            return memo[(i, j, f, b)]
        
        res = 0
        for k in range(i, j + 1):
            if prime[k]:
                if (f and prime[k] in bad_primes) or (not f and not prime[k] in bad_primes):
                    res += beauty(i, k - 1, not f, 1 - b)
                else:
                    res = max(res, beauty(i, k - 1, not f, 0))
            else:
                res = max(res, beauty(i, k - 1, f, b))
        
        memo[(i, j, f, b)] = res
        return res
    
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))
    
    print(beauty(0, n - 1, True, False))
