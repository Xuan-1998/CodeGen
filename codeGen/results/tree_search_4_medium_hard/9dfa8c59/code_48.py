def count_primes(n, k):
    memo = {}
    if n in memo:
        return memo[n]
    
    if not is_prime(n):  # Check if n is prime
        return 0
    
    result = [n, n]  # Initialize the result with the current number and its own permutations
    
    for d in str(n):
        perms = k * factorial(len(str(n)) - 1)  # Calculate the number of permutations
        if perms == k_perms:  # Check if the calculated count is equal to k_perms
            return [n, result[0], result[1]]
        
        new_k = k + 1
        if (n, new_k) in memo:
            return memo[(n, new_k)]
        
        new_result = count_primes(int(str(n).replace(d, '')), new_k)
        if new_result:
            return new_result
        
    memo[n] = [0, 0, 0]  # Store the result for future reference
    return memo[n]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    n_max, k_perms = map(int, input().split())
    result = count_primes(n_max, k_perms)
    print(*result, sep='\n')
