import sys

def can_send_sequence(b):
    n = len(b)
    for i in range(1, n + 1):
        prefix_sum = sum(b[:i])
        if prefix_sum == b[i - 1]:
            return True
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print("YES" if can_send_sequence(b) else "NO")
