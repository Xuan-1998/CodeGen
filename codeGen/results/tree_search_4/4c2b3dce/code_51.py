import sys

def find_AB(s):
    s = s.upper()
    for i in range(len(s) - 2):  # Consider a sliding window of size 3
        if s[i:i+2] == "AB" or s[i:i+2] == "BA":  
            remaining_str = s[i+2:] 
            if (remaining_str.count("A") == 1 and remaining_str.count("B") == 1) or \
               (remaining_str.count("B") == 1 and remaining_str.count("A") == 1):
                return "YES"
    return "NO"

# Receive input from stdin
s = sys.stdin.readline().strip()

print(find_AB(s))
