import sys

s = input().strip()

ab_state = 0
ba_state = 0

for c in s:
    if c == 'A':
        ab_state += 1
        ba_state = 0
    elif c == 'B':
        ba_state += 1
        ab_state = 0
    
    if ab_state and ba_state:
        print("YES")
        sys.exit(0)

print("NO")
