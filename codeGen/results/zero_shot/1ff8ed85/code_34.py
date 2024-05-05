import sys

def can_send_over_network(b):
    n = len(b)
    for i in range(n // 2 + 1):
        a = []
        left_len = 0
        right_len = 0
        for j in range(i, n - i):
            if b[j] == i:
                left_len += i
            elif b[n - j - 1] == i:
                right_len += i
            else:
                a.append(b[j])
                if j < n // 2:
                    left_len += len(a) + 1
                else:
                    right_len += len(a) + 1
        if (n - left_len) % (len(a) + 1) == 0 and (n - right_len) % (len(a) + 1) == 0:
            return "YES"
    return "NO"

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    print(can_send_over_network(b))
