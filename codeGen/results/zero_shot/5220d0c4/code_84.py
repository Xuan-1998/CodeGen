n, m = map(int, input().split())  # Read n and m from stdin
arr = list(map(int, input().split()))  # Read array elements from stdin
bad_primes = list(map(int, input().split()))  # Read bad prime numbers from stdin

max_beauty = 0
for num in arr:
    max_beauty = max(max_beauty, beauty(num, bad_primes))

print(max_beauty)  # Output the maximum beauty to stdout
