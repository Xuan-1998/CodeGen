def can_send_over_network():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        if any(b[i] > 0 and b[i-1] <= 0 for i in range(1, n)):
            print('YES')
        else:
            print('NO')

can_send_over_network()
