import sys

def can_send_b_over_network(b):
    n = len(b)
    for i in range(1, n+1):
        for j in range(i, n+1):
            seg_lengths = [str(len(str(b[k:i])))] * (j-i)
            if ''.join(seg_lengths) == ''.join(map(str, b)):
                return True
    return False

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    print('YES' if can_send_b_over_network(b) else 'NO')
