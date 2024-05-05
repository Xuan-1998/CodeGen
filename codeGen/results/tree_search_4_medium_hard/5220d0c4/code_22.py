def min_prime_divisor(n):
    if n % 2 == 0:
        return 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return i
    return n

def beauty(i, prev_min_divisor):
    if i < 1:
        return 0
    min_divisor = min_prime_divisor(i)
    if min_divisor != prev_min_divisor:
        return max(beauty(i - 1, min_divisor), beauty(i - 1, prev_min_divisor) + i)
    else:
        return beauty(i - 1, min_divisor)

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    max_beauty = 0
    for i in range(n):
        max_beauty = max(max_beauty, beauty(i, -1))

    print(max_beauty)

if __name__ == "__main__":
    main()
