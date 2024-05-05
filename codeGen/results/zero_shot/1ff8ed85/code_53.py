def can_send_over_network(b):
    n = len(b)
    
    for i in range(1, n+1):
        a = [0] + b[:i] + [len(str(i))]
        
        for j in range(i, 0, -1):
            a[j-1] = str(a[j-1]) + str(len(str(j)))
            
        if ''.join(map(str, a)) == ''.join(map(str, b)):
            return 'YES'
    
    return 'NO'

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print(can_send_over_network(b))
