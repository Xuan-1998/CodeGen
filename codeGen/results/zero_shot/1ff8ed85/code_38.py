def can_send_over_network(b):
    n = len(b)
    prev_val = b[0]
    inc_count = 0
    dec_count = 0
    
    for i in range(1, n):
        if b[i] <= prev_val:
            inc_count += 1
        elif b[i] > prev_val:
            dec_count -= 1
        prev_val = b[i]
    
    return inc_count > dec_count

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    if can_send_over_network(b):
        print("YES")
    else:
        print("NO")
