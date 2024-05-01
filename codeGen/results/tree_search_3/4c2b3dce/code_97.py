def solve():
    s = input().strip()
    n = len(s)
    
    # Base case: if length is less than 3, we can directly check for 'AB' and 'BA'
    if n < 3:
        return "YES" if s in ['AB', 'BA'] else "NO"
    
    # Find the first occurrence of 'A' or 'B'
    i = j = 0
    while i < n and (s[i] not in 'AB' or (j > 0 and s[i] == s[j-1])):
        if s[i] == 'A':
            j = i
        i += 1
    
    # If we didn't find any 'A' or 'B', then it's impossible to have 'AB' and 'BA'
    if i == n:
        return "NO"
    
    # Check for 'AB' and 'BA' in the remaining string
    rest = s[i:]
    if 'AB' in rest and 'BA' in rest:
        return "YES"
    else:
        return "NO"

print(solve())
