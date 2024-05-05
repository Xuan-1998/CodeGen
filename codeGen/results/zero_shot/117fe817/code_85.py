import math

def count_digit_one(n):
    total = 0
    for i in range(1, n+1):
        # Calculate the length of the integer i
        len_i = int(math.log10(i)) + 1
        
        # Count the number of times digit 1 appears in i
        total += min(len_i, i)
    
    return total

n = int(input())
print(count_digit_one(n))
