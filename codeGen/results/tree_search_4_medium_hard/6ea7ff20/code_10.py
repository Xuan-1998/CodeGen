def merge(a, b):
    if not a:
        return b
    if not b:
        return a

    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    elif a[0] > b[0]:
        return [b[0]] + merge(a, b[1:])
    else:
        raise ValueError("Arrays should have no common elements")

def check_merge(p):
    n = len(p) // 2
    for i in range(1 << (n - 1)):
        a = []
        b = []
        j = 0
        for k in range(n - 1, -1, -1):
            if ((i >> k) & 1):
                a.append(p[j])
                j += 1
            else:
                b.append(p[j])
                j += 1
        if len(a) + len(b) == len(p):
            for k in range(n - 1, -1, -1):
                p[k] = (i >> k) & 1 and a.pop() or b.pop()
            return "YES"
    return "NO"

while True:
    n = int(input())
    if n == 0:
        break
    p = list(map(int, input().split()))
    print(check_merge(p))
