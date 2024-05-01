import sys

def find_substrings():
    s = input().strip()
    
    has_ab, has_ba = False, False
    
    for i in range(len(s) - 1):
        if s[i:i+2] == 'AB':
            has_ab = True
        elif s[i:i+2] == 'BA':
            has_ba = True
            
        if has_ab and has_ba:
            break
            
    if has_ab and has_ba:
        print("YES")
    else:
        print("NO")

find_substrings()
