def merge(a, b):
    result = []
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    result.extend(a)
    result.extend(b)
    return result

def solve(n, p):
    for i in range(2n):
        if (i < n and p[i] > p[n - 1]) or (i >= n and p[i] < p[2n - 1]):
            return "NO"
    return "YES"

while True:
    try:
        n = int(input())
        p = list(map(int, input().split()))
        print(solve(n, p))
    except EOFError:
        break
