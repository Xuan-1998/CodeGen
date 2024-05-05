python
# Step 1: Read the input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

# Step 2: Pre-compute the minimum prime divisor for each number in the array
min_prime_divisors = {}
for i in range(2, max(arr) + 1):
    if is_prime(i):
        min_prime_divisors[i] = i
    else:
        j = 2
        while j * j <= i:
            if i % j == 0:
                min_prime_divisors[i] = j
                break
            j += 1

# Step 3: Calculate the beauty of each number in the array
beauties = [min_prime_divisors[x] if x in bad_primes else max(min_prime_divisors[x], x) for x in arr]

# Step 4: Find the maximum beauty
max_beauty = max(beauties)

print(max_beauty)
