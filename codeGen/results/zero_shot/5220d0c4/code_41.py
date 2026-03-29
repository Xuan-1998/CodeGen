def find_bad_primes(n):
    bad_primes = []
    for i in range(2, n+1):
        if is_prime(i) and not is_good_prime(i):
            bad_primes.append(i)
    return bad_primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_minimum_prime_divisors(arr):
    min_primes = []
    for num in arr:
        prime_divisor = num
        for i in range(2, int(prime_divisor**0.5) + 1):
            if prime_divisor % i == 0:
                prime_divisor = i
                break
        min_primes.append(prime_divisor)
    return min_primes

def calculate_beauty(arr, bad_primes):
    beauty = 0
    for num in arr:
        if num in bad_primes:
            beauty += num * 2
        else:
            prime_divisor = find_minimum_prime_divisors([num])[0]
            beauty += prime_divisor * 2
    return beauty

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))
    print(calculate_beauty(arr, bad_primes))

if __name__ == "__main__":
    solve()
