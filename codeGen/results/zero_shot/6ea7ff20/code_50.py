def merge(a, b):
    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a
    else:
        if a[0] < b[0]:
            return [a[0]] + merge(a[1:], b)
        else:
            return [b[0]] + merge(a, b[1:])

def check(p):
    n = len(p) // 2
    a = []
    for i in range(n):
        a.append(p[i])
    b = p[n:]
    if merge(a, b) == p:
        return "YES"
    else:
        return "NO"

n = int(input())
p = list(map(int, input().split()))
print(check(p))
