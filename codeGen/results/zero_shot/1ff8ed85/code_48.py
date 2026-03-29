def can_send_b_over_network(b):
    n = len(b)
    curr_a = 0
    for i in range(n):
        if b[i] > curr_a + 1:
            return False
        curr_a += b[i]
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print("YES" if can_send_b_over_network(b) else "NO")
