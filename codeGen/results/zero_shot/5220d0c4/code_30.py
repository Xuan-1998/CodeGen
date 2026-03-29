# Read input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

# Function to find minimum prime divisor for a number
def min_prime_divisor(num):
    # Check if the number is itself (in that case it has no prime divisors)
    if num == 1:
        return None

    # Initialize i at 2 and increment by 2 in each iteration to reduce 
    # unnecessary calculations by half.
    i = 2
    while(i * i <= num):
        if(num % i):
            i += 1
        else:
            break
    return i

# Function to calculate beauty for an array
def calculate_beauty(arr, bad_primes):
    beauty = 0
    for num in arr:
        min_divisor = min_prime_divisor(num)
        # Check if the number is not a bad prime or its minimum divisor is 
        # greater than the number itself (in that case it has no prime divisors)
        if min_divisor not in bad_primes and min_divisor > num:
            beauty += 1
    return beauty

# Calculate maximum beauty by trying all possible subsets of the array
max_beauty = 0
for i in range(2**n):
    subset_arr = [arr[j] for j in range(n) if (i & (1 << j))]
    max_beauty = max(max_beauty, calculate_beauty(subset_arr, bad_primes))

# Print the maximum beauty of the array
print(max_beauty)
