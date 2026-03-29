import sys

def count_digit_ones(n):
    # Initialize the total count
    total_count = 0
    
    for i in range(1, n + 1):
        # Count the number of digit 1s in each power of 10
        if '1' in str(i):
            total_count += str(i).count('1')
    
    print(total_count)

if __name__ == "__main__":
    n = int(sys.stdin.read())
    count_digit_ones(n)
