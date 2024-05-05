# Step 1: Read input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

# Step 2: Create a dictionary to store prime numbers and their indices in the array
prime_dict = {}

# Step 3: Function to find the minimum prime divisor of a number
def min_prime_divisor(num):
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            return i
    return num

# Step 4: Calculate beauty for each element in the array
beauty_arr = [min_prime_divisor(num) if num in bad_primes else 1 for num in arr]

# Step 5: Function to calculate the maximum beauty of the array
def max_beauty(arr):
    return sum(1 for x in arr if x > 0)

# Step 6: Calculate and print the maximum beauty
print(max_beauty(beauty_arr))
