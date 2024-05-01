import sys

def check_string():
    s = input()
    
    seen = [False, False]
    has_ab = False
    
    for c in s:
        if c == 'A':
            seen[0] = True
            if seen[1]:
                has_ab = True
            else:
                seen[1] = True
        elif c == 'B':
            seen[1] = True
            if not seen[0]:
                has_ab = True
    
    if has_ab and seen[0] and seen[1]:
        print("YES")
    else:
        print("NO")

check_string()
