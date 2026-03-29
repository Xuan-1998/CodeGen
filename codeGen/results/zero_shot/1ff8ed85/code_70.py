import sys

def can_send_sequence(b):
    n = len(b)
    for i in range(1, n):
        if abs(b[i] - b[0]) != i:
            return "NO"
    return "YES"

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    print(can_send_sequence(b))
