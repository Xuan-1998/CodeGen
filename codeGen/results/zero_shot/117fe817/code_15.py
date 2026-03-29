import math

def count_digit1(n):
    total = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:  # i is a factor of n
            factors = 2  # i and n//i are both factors
            while i * i <= n:
                j = math.floor(math.sqrt(n // i))
                if j * j == n // i:
                    break
                j += 1
                factors += 2 * (j - i)
                i = j
            total += factors
    return total

n = int(input())
print(count_digit1(n))
