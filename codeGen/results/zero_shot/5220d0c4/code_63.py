def beauty(arr, bad_primes):
    total_beauty = 0
    for num in arr:
        min_divisor = min_prime_divisor(num)
        if is_good_prime(min_divisor):
            # TO DO: Calculate the beauty based on whether it's a good prime or not
            pass
        else:
            # TO DO: Handle bad primes separately
            pass
        total_beauty += ?  # Update the total beauty
    return total_beauty

# Example usage:
arr = [1, 2, 3, 4]
bad_primes = [2, 3]
print(beauty(arr, bad_primes))
