import sys

def find_ABBA(s):
    A_prev = False
    B_prev = False
    found_A = False
    found_B = False
    
    for char in s:
        if char == 'A':
            A_prev, B_prev = True, A_prev
            found_A = not found_A
        elif char == 'B':
            B_prev, A_prev = True, B_prev
            found_B = not found_B
        
        if A_prev and B_prev and found_A and found_B:
            return "YES"
    
    return "NO"

s = input()
print(find_ABBA(s))
