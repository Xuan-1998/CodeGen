def can_send_over_network(b):
    n = len(b)
    for i in range(1, n):
        if b[i-1] > 0 and b[i] > 0:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print(can_send_over_network(b))
