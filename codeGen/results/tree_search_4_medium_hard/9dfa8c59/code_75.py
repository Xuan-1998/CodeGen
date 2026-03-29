def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_permutation(n):
    """Calculate the number of permutations for a given number."""
    # Use a set to keep track of unique digits
    digits = set(int(digit) for digit in str(n))
    # Calculate the number of permutations by multiplying the factorial of each digit's count
    permutations = 1
    for digit in digits:
        permutations *= math.factorial(len(str(digit)))
    return permutations

def main():
    n_max, k_perms = map(int, input().split())
    
    prime_count = 0
    smallest_prime = float('inf')
    largest_prime = 0
    
    memo = {}
    
    for i in range(2, n_max + 1):
        if is_prime(i):
            if i not in memo or memo[i] is None:
                memo[i] = is_permutation(i)
            if memo[i] == k_perms:
                prime_count += 1
                smallest_prime = min(smallest_prime, i)
                largest_prime = max(largest_prime, i)
    
    print([prime_count, smallest_prime, largest_prime])

if __name__ == "__main__":
    main()
