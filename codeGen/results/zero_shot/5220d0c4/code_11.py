def get_bad_primes(n, m):
    # Read bad prime numbers from input
    bad_primes = list(map(int, input().split()))
    return bad_primes

def find_max_beauty(arr, bad_primes):
    # Calculate beauty for each number in the array
    beauties = []
    for num in arr:
        min_divisor = 2
        while num % min_divisor != 0:
            min_divisor += 1
        is_bad_prime = any(min_divisor == prime for prime in bad_primes)
        beauty = 1 if not is_bad_prime else -1
        beauties.append(beauty)

    # Find the maximum beauty
    max_beauty = max(beauties)

    return max_beauty

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = get_bad_primes(n, m)
    print(find_max_beauty(arr, bad_primes))

if __name__ == "__main__":
    main()
