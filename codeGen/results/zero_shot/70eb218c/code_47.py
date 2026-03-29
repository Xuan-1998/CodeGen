import sys

def convert_decimal(n, x):
    # Convert decimal representation of x into binary
    binary = str(bin(x))[2:]
    
    # Pad with leading zeros if necessary
    while len(binary) < n:
        x *= 2
        binary = str(bin(x))[2:]
    
    return len(binary)

n, x = map(int, input().split())
if n > 0 and 1 <= x < 10**(n-1):
    print(convert_decimal(n, x))
else:
    print(-1)
