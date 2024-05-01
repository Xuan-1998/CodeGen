import sys

# Read input from stdin
s = sys.stdin.readline().strip()

found_AB = False
found_BA = False

for i in range(len(s) - 1):
    if s[i:i+2] == 'AB' and not found_AB:
        found_AB = True
    elif s[i:i+2] == 'BA' and not found_BA:
        found_BA = True
        
# Check if we have found both substrings
if found_AB and found_BA:
    print('YES')
else:
    print('NO')
