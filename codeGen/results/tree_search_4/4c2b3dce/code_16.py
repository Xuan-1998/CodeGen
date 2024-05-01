import sys

def check_string(s):
    if len(s) < 2:
        return "YES"
    
    for i in range(len(s)-1):
        if s[i:i+2] == 'AB' and s[i+2:] == s[:i][::-1]:
            return "YES"

    return "NO"


# Read input from stdin
s = sys.stdin.readline().strip()

# Print the result to stdout
print(check_string(s))
