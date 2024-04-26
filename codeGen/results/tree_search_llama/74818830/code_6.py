import math

def odd_factors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if math.pow(i, 2) <= n:
            if math.gcd(i, n // i) == 1:  # Check if i is relatively prime to n//i (i.e., the square root of n)
                count += 1
    return count

n = int(input())  # Read input from stdin
print(odd_factors(n))  # Print the result to stdout
