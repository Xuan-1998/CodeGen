n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

beauties = []
for num in arr:
    is_bad_prime = num in bad_primes
    beauty_val = beauty(num, is_bad_prime)
    beauties.append(beauty_val)

print(sum(beauties))
