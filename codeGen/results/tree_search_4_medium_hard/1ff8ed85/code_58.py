def can_send_over_network():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        even = True
        odd = False
        
        for length in b:
            if length % 2 == 0:
                even = (even and True) or (odd and False)
                odd = False
            else:
                even = False
                odd = (odd and True) or (even and False)
        
        print('YES' if even else 'NO')

can_send_over_network()
