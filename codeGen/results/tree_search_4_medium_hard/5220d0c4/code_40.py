import sys

def min_prime_divisor(n):
    if n < 2:
        return 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n

def calculate_beauty(array, bad_primes):
    n = len(array)
    beauty_values = [[0] * (1 << n) for _ in range(n)]
    
    # Calculate the minimum prime divisor of each element.
    min_prime_divisors = [min_prime_divisor(num) for num in array]
    
    for subset_idx in range(2**n):
        subset_sum = 0
        for elem_idx, elem in enumerate(array):
            if (subset_idx >> elem_idx) & 1:
                subset_sum += min_prime_divisors[elem_idx]
        
        # Calculate the beauty of this subset.
        beauty_values[0][subset_idx] = subset_sum
        
    max_beauty = max(max(row) for row in beauty_values)
    
    return max_beauty

def main():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))
    
    print(calculate_beauty(array, bad_primes))

if __name__ == "__main__":
    main()
