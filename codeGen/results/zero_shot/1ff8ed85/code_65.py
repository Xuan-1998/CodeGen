import sys

def check_transform(a, b):
    n = len(b)
    for i in range(n):
        a[i] += [0, b[i]]  # write length to left or right of segment
    return ''.join(map(str, a)) == ''.join(map(str, b))

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    if check_transform(a, b):
        print("YES")
    else:
        print("NO")
