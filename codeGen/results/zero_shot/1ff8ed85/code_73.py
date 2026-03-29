import sys

def can_send_sequence(b):
    n = len(b)
    for i in range(1, n+1):
        a = [str(len(str(i)))] + list(map(str, b))
        if ''.join(a) == ''.join(map(str, b)):
            return "YES"
    return "NO"

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    print(can_send_sequence(b))
