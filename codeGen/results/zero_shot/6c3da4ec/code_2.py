import sys

def max_bitwise_or(s):
    n = len(s)
    max_or = 0
    
    # Generate all possible pairs of non-empty substrings
    for i in range(n):
        for j in range(i + 1, n):
            sub1 = int(s[i:j+1], 2)  # Convert binary substring to integer
            for k in range(j + 1, n):
                sub2 = int(s[j:k+1], 2)
                or_val = sub1 | sub2  # Calculate bitwise OR of two substrings
                max_or = max(max_or, or_val)  # Update maximum OR value
    
    return bin(max_or)[2:]  # Convert maximum OR value to binary and remove '0b' prefix

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
print(max_bitwise_or(s))
