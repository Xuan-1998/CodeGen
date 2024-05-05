import sys

def max_bitwise_or(s):
    n = len(s)
    max_or_value = 0
    
    for i in range(n):  # iterate over all possible starting positions
        for j in range(i + 1, n):  # iterate over all possible ending positions
            substring1 = int(s[i:j], 2)  # convert substring to integer and perform bitwise OR
            substring2 = int(s[j:] + s[:i], 2)  # convert remaining substring to integer and perform bitwise OR
            or_value = substring1 | substring2
            max_or_value = max(max_or_value, or_value)
    
    return bin(max_or_value)[2:].zfill(n).lstrip('0')  # convert maximum OR value to binary and remove leading zeroes

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
print(max_bitwise_or(s))
