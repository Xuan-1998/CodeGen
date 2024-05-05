n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + (1 if is_bad_prime(min_prime_divisor(arr[i])) else -1)

max_beauty = max(prefix_sum[i] for i in range(1, n+1))

print(max_beauty)
