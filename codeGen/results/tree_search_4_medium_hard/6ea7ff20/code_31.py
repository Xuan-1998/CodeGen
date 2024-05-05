def merge(a, b):
    res = []
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            res.append(a.pop(0))
        else:
            res.append(b.pop(0))
    return res + list(a) + list(b)

def check(p, n):
    a = [i for i in range(n)]
    b = [i for i in range(n, 2*n)]
    if p == merge(set(a), set(b)):
        return "YES"
    else:
        return "NO"

n = int(input())
p = list(map(int, input().split()))
print(check(p, n))
