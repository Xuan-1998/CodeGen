import sys

def get_prime_permutations(n):
    # Base case: single digit prime number has 1 permutation
    if n < 10:
        return [n]

    # Recursive case: calculate permutations for each digit
    digits = [int(d) for d in str(n)]
    perms = [d]
    for d in digits[1:]:
        perms = [p + str(d) for p in perms] + [str(d) + p for p in perms]
    return list(set(perms))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n_max, k_perms = map(int, sys.stdin.readline().split())
    
    primes = set()
    for num in range(2, n_max+1):
        if is_prime(num):
            primes.add(num)

    count = 0
    smallest = largest = 0
    for prime in primes:
        perms = get_prime_permutations(str(prime))
        if len(perms) == k_perms:
            count += 1
            if not smallest:
                smallest = prime
            else:
                largest = max(largest, prime)

    print([count, smallest, largest])

if __name__ == "__main__":
    main()
