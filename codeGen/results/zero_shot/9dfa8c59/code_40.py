def find_prime_permutations():
    n_max = int(input())  # Read input from standard input
    k_perms = int(input())
    
    count = 0  # Initialize count of prime numbers with k_perms permutations below n_max
    smallest_prime = float('inf')  # Initialize smallest prime number
    largest_prime = 0  # Initialize largest prime number
    
    for num in range(2, n_max):  # Iterate from 2 to n_max (inclusive)
        if is_prime(num):  # Check if the current number is prime
            permutations = count_permutations(str(num))  # Count permutations of the digits of the current number
            
            if permutations == k_perms:  # If the number has exactly k_perms permutations
                count += 1  # Increment the count
                smallest_prime = min(smallest_prime, num)  # Update smallest prime number
                largest_prime = max(largest_prime, num)  # Update largest prime number
    
    return [count, smallest_prime, largest_prime]  # Return the count and smallest/largest prime numbers

def is_prime(num):
    if num < 2:  # If the number is less than 2, it's not prime
        return False
    for i in range(2, int(num**0.5) + 1):  # Check divisibility from 2 to sqrt(n)
        if num % i == 0:
            return False
    return True

def count_permutations(digits):
    n = len(digits)  # Get the length of the digits string
    permutations = 1  # Initialize permutation count
    
    for digit in digits:  # Iterate over each digit
        index = 0  # Initialize an index variable
        while index < n and index <= int(digit):  # While the current digit is less than or equal to the next digit
            index += 1  # Increment the index
        permutations *= (index)  # Update the permutation count
    
    return permutations

print(find_prime_permutations())
