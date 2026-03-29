import sys

def max_bitwise_or(s):
    n = len(s)
    # Initialize max_val to the maximum possible value (2^n - 1)
    max_val = (1 << n) - 1
    
    for c in s:
        # Update max_val by performing bitwise OR with each character
        max_val &= max_val | int(c)

    return bin(max_val)[2:]

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    
    print(max_bitwise_or(s))
