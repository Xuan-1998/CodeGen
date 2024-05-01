from collections import defaultdict

def solve():
    s = input()
    n = len(s)
    
    memo = defaultdict(bool)
    for i in range(n):
        if s[i:i+2] == 'AB':
            if i + 2 >= n or s[i+2] != 'A':
                memo[''.join([s[:i], s[i+2:]]).lstrip('A').rstrip('B')] = True
        elif s[i:i+2] == 'BA':
            if i + 2 >= n or s[i+2] != 'B':
                memo[''.join([s[:i], s[i+2:]]).lstrip('B').rstrip('A')] = True
    
    for i in range(n):
        if memo[s[:i]]:
            return 'YES'
    
    return 'NO'

print(solve())
