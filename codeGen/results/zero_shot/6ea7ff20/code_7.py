import sys

def merge(a, b):
    if not a and not b:
        return []
    elif not a:
        return b
    elif not b:
        return a
    else:
        if a[0] < b[0]:
            return [a[0]] + merge(a[1:], b)
        else:
            return [b[0]] + merge(a, b[1:])

def solve():
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    
    # Check if the permutation is valid
    if len(p) != 2 * n or any(x < y for x, y in zip(p[:n], p[n:])):
        print("NO")
        return
    
    # Try to split the permutation into two arrays a and b
    a = []
    b = []
    for i in range(n):
        if p[i] <= p[-1 - i]:
            a.append(p[i])
        else:
            b.append(p[i])
    
    if len(a) + len(b) == 2 * n:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
