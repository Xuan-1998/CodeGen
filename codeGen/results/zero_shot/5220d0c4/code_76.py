n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

max_beauty = 0
for _ in range(100):  # TO DO: implement a better loop
    max_beauty = max(max_beauty, beauty(arr, bad_primes))

print(max_beauty)
