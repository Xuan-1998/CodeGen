# Step 1: Read input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

# Step 2: Find all prime numbers in the array and separate them into good and bad primes
good_primes = [num for num in arr if is_prime(num) and num not in bad_primes]
bad_primes_in_arr = [num for num in arr if is_prime(num) and num in bad_primes]

# Step 3: Calculate the beauty of each number in the array
beauties = []
for num in arr:
    min_divisor = find_min_prime_divisor(num)
    if min_divisor in good_primes:
        beauty = 1
    elif min_divisor in bad_primes_in_arr:
        beauty = -1
    else:
        beauty = 0
    beauties.append(beauty)

# Step 4: Calculate the maximum beauty of the array by finding the maximum sum of a subset
max_beauty = max(subset_sum(beauties, i) for i in range(len(beauties)))

print(max_beauty)
