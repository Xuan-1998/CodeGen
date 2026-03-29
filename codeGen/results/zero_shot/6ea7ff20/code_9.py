def merge(a, b):
    if not a and b:
        return b
    elif a and not b:
        return a
    elif a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

def solve(n):
    p = list(map(int, input().split()))
    result = "YES"
    
    for i in range(2*n):
        x = p[i]
        if i < n:
            a.append(x)
        else:
            b.append(x)
    
    if len(set(a+b)) != 2*n:
        result = "NO"
    
    print(result)

n = int(input())
a, b = [], []
solve(n)
