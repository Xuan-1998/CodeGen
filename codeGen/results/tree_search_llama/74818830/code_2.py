def count_odd_factors(N):
    count = 0
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            exp_i = 0
            while N % (i ** (exp_i + 1)) == 0:
                exp_i += 1
            if exp_i % 2 != 0:  # If the exponent is odd, increment the count
                count += 1
    return count

# Read input from stdin
N = int(input())

# Print the output to stdout
print(count_odd_factors(N))
