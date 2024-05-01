import sys

def find_substr(s):
    if len(s) < 2:
        return "NO"

    i = 0
    while i < len(s):
        if s[i] == 'A':
            j = i + 1
            while j < len(s) and s[j] != 'B':
                j += 1
            if j < len(s) and s[j] == 'B':
                k = j + 1
                while k < len(s):
                    if s[k] == 'A' and s[k+1] == 'B':
                        return "YES"
                    k += 1
        i += 1

    return "NO"

# Read input from stdin
s = sys.stdin.readline().strip()

print(find_substr(s))
