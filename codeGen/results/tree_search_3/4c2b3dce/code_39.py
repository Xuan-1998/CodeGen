from collections import defaultdict

def solve():
    s = input()
    dp = defaultdict(bool)
    a_count, b_count = 0, 0
    
    for c in s:
        if c == 'A':
            a_count += 1
        else:
            b_count += 1
        
        if (a_count > 0 and b_count > 0):
            dp[(a_count, b_count)] = (a_count == 1) | dp.get((b_count-1, a_count), False)
    
    return "YES" if any(dp.values()) else "NO"

print(solve())
