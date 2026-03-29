import sys

def can_form_b(a, b):
    a_segments = [str(len(x)) for x in a]
    for i, (x, y) in enumerate(zip(b, a_segments)):
        if str(y) != x:
            return False
    return True

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    if can_form_b([str(len(x)) for x in [1] * n], b):
        print('YES')
    else:
        print('NO')
