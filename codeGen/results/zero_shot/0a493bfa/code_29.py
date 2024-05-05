import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def beauty(array):
    result = 0
    for num in array:
        prime_factors = []
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                prime_factors.append(i)
        if num > 1:
            prime_factors.append(num)
        beauty = 0
        for factor in prime_factors:
            if factor not in bad_primes:
                beauty += factor
        result += beauty
    return result

def main():
    n, m = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))
    bad_primes = list(map(int, sys.stdin.readline().split()))

    print(beauty(array))

if __name__ == "__main__":
    main()
