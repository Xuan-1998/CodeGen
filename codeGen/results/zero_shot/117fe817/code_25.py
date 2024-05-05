import sys

def count_digit_ones(n):
    total_ones = 0
    
    # Count ones in single-digit numbers
    total_ones += 1
    
    # Count ones in two-digit numbers
    total_ones += 10 * (n // 10)
    
    # Count ones in three-digit numbers
    total_ones += 100 * ((n // 100) + (n % 100) // 10)
    
    # Count ones in four-digit numbers
    if n >= 1000:
        total_ones += 10000
    
    return total_ones

if __name__ == "__main__":
    n = int(sys.stdin.read())
    print(count_digit_ones(n))
