def min_prime_divisor(n):
    if n < 2:
        return None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n

def beauty(arr, bad_primes):
    beauty = 0
    for num in arr:
        div = min_prime_divisor(num)
        if div not in bad_primes:
            beauty += 1
    return beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

arr.sort()
bad_primes.sort()

max_beauty = 0
for i in range(n):
    for j in range(i+1, n):
        if min_prime_divisor(arr[i]) == min_prime_divisor(arr[j]):
            max_beauty = max(max_beauty, beauty(arr[:i] + arr[i+1:j] + arr[j:], bad_primes))

print(max_beauty)
