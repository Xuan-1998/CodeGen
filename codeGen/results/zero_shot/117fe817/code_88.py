import sys

def count_digit_ones(n):
    total_ones = 0
    
    for i in range(n+1):
        ones_count = str(i).count('1')
        total_ones += ones_count
    
    return total_ones

n = int(sys.stdin.readline())
print(count_digit_ones(n))
