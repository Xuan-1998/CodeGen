def can_send_over_network(t):
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        a = []
        for i in range(n-1):
            a.append(b[i])
        
        if len(a) != 0 and (a[0] == 0 or a[-1] == 0):
            print("NO")
        else:
            print("YES")

t = int(input())
can_send_over_network(t)
