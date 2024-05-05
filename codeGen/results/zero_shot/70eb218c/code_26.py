import sys

def min_operations(n, x):
    # Convert x into its decimal representation as a string
    s = str(x)
    
    # Calculate the current length of the decimal representation
    curr_len = len(s)
    
    if curr_len == n:
        return 0
    
    operations = 0
    i = 0
    while i < curr_len and i < n:
        digit = int(s[i])
        for y in range(1, 10):
            new_digit = digit * y
            new_len = len(str(new_digit))
            if new_len == n - i - 1:
                x *= new_digit
                operations += 1
                break
        else:
            return -1
        i += 1
    
    return operations

n, x = map(int, input().split())
print(min_operations(n, x))
