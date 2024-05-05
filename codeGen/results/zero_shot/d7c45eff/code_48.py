import sys

def smallest_string(n, k):
    s = input().strip()
    
    if k <= n:
        return s[:k]
    
    if k > n:
        last_char = s[-1]
        remaining_str = s[:-1]
        
        if remaining_str < last_char:
            return s
        else:
            return s + last_char
    
    return ""

n, k = map(int, input().split())
print(smallest_string(n, k))
