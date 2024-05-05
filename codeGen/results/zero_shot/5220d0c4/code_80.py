# Step 1: Read input
n, m = map(int, input().split())  # array size and number of bad prime numbers
arr = list(map(int, input().split()))  # elements of the array
bad_primes = list(map(int, input().split()))  # bad prime numbers

# Step 2: Find all prime numbers up to max(arr)
max_val = max(arr)
prime_numbers = []
for i in range(2, max_val + 1):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(i)

# Step 3: Filter out bad primes from the list of prime numbers
good_primes = [i for i in prime_numbers if i not in bad_primes]

# Step 4: Calculate the beauty of each number in the array using its minimum good prime divisor
beauties = []
for num in arr:
    min_divisor = num
    for prime in good_primes:
        if num % prime == 0 and prime < min_divisor:
            min_divisor = prime
    beauties.append(min_divisor)

# Step 5: Find the maximum beauty of the array
max_beauty = max(beauties)

# Step 6: Print the answer
print(max_beauty)
