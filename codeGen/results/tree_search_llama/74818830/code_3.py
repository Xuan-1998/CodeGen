import math

def count_odd_divisors(N):
    count = 0
    for i in range(1, int(math.sqrt(N)) + 1):
        if i ** 2 <= N:
            count += 1
    return count

N = int(input())  # Read the input from standard input
print(count_odd_divisors(N))  # Print the result to standard output
