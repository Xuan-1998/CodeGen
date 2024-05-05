import math

def count_digit_ones(n):
    last_position = math.floor(n / 10)
    
    first_position = min(9, n // 10)  # We don't need to consider numbers that start with "100" or more.
    
    middle_positions = (n // 100 + 1) if n >= 100 else 0
    
    return last_position + first_position + middle_positions

if __name__ == "__main__":
    n = int(input())
    print(count_digit_ones(n))
