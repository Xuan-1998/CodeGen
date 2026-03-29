import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def max_beauty(n, m, arr, bad_primes):
    table = [[-1] * (n+1) for _ in range(m+1)]
    table[0][0] = 0
    
    for p in range(2, m+1):
        if is_prime(p):
            bad_primes.remove(p)
    
    for i in range(n+1):
        for j in range(min(i, m)+1):
            if arr[i-1] % bad_primes[j-1] == 0:
                table[j][i] = max(table[j][i-1], 1 + (not is_prime(arr[i-1])))
            else:
                table[j][i] = table[j][i-1]
    
    return max(max(row) for row in table)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(n, m, arr, bad_primes))
