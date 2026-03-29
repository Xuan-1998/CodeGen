import sys

def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

def check_permutation(p):
    n = len(p) // 2
    
    for i in range(n):
        a = p[:i+1]
        b = p[i+1:]
        
        if any(x in y for x in a for y in b):
            return "NO"
    
    return "YES"

n = int(sys.stdin.readline())
p = [int(x) for x in sys.stdin.readline().split()]
print(check_permutation(p))
