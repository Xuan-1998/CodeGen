def is_good_prime(n):
    for prime in bad_primes:
        if n % prime == 0:
            return "bad"
    return "good"

def calculate_beauty(arr):
    beauty = 0
    for num in arr:
        if is_good_prime(num) == "good":
            beauty += min(prime_factors(num))
        else:
            beauty -= min(prime_factors(num))
    return beauty

def prime_factors(n):
    factors = []
    for i in range(2, n+1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if not factors:
        factors.append(n)
    return factors

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))
    max_beauty = 0
    for i in range(n):
        temp_arr = arr[:i] + arr[i+1:]
        beauty = calculate_beauty(temp_arr)
        if beauty > max_beauty:
            max_beauty = beauty
    print(max_beauty)

main()
