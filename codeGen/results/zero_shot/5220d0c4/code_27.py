import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n

def max_beauty(n, bad_primes, primes):
    beauty = 0
    for num in range(2, n+1):
        prime_divisor = next_prime(num)
        if prime_divisor > num:  # No need to check further
            break
        if is_prime(prime_divisor) and prime_divisor not in bad_primes:
            beauty += 1
    return beauty

def main():
    n, m = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))
    bad_primes = list(map(int, sys.stdin.readline().split()))
    
    primes = []
    for i in range(2, 1000000):  # Generate all prime numbers up to a certain limit
        is_prime_num = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime_num = False
                break
        if is_prime_num and i not in bad_primes:
            primes.append(i)
    
    print(max_beauty(n, bad_primes, primes))

if __name__ == "__main__":
    main()
