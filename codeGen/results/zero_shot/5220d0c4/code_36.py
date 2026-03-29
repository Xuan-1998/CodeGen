def find_max_beauty():
    n, m = map(int, input().split())  # Read the size of the array and the number of bad prime numbers
    arr = list(map(int, input().split()))  # Read the elements of the array
    bad_primes = list(map(int, input().split()))  # Read the bad prime numbers

    max_beauty = 0  # Initialize the maximum beauty found so far
    for i in range(n):
        min_prime_divisor = find_min_prime_divisor(arr[i], bad_primes)  # Find the minimum prime divisor of each element
        arr[i] = min_prime_divisor if is_good_prime(min_prime_divisor) else -min_prime_divisor  # Calculate the beauty of the array

    return sum(arr)

def find_min_prime_divisor(num, bad_primes):
    for i in range(2, num + 1):  # Iterate from 2 to the number
        if is_prime(i) and i not in bad_primes:  # If it's a prime number that's not bad
            return i  # Return the minimum prime divisor

def is_good_prime(num):
    # Define what makes a prime number "good"
    # For example, we could consider all prime numbers greater than 3 as good
    if num > 3:  # Check if the prime number is good
        return True  # If it's good, return True

def main():
    print(find_max_beauty())  # Call the function to find the maximum beauty

if __name__ == "__main__":
    main()
