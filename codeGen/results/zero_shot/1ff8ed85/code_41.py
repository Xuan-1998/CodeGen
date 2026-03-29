def can_send_sequence(b):
    n = len(b)
    for i in range(n):
        if b[i] > 0:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print(can_send_sequence(b))
