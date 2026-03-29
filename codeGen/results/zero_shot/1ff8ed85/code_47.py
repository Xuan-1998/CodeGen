def can_send_over_network(b):
    n = len(b)
    
    # Check if b is a valid sequence
    for i in range(n - 1):
        if abs(b[i] - b[i + 1]) > 1:  # A segment cannot be more than one length away from the next
            return "NO"
    
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print(can_send_over_network(b))
