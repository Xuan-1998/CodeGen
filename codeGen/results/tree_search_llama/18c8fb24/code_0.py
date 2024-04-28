def will_ball_enter_hole():
    T = int(input())
    
    for _ in range(T):
        N, x, k = map(int, input().split())
        
        if x % (2*k) == 0 or (N+1) % (2*k) == 0:
            print("YES")
        else:
            remainder = (N+1) % (2*k)
            
            if remainder == x:
                print("YES")
            else:
                print("NO")

will_ball_enter_hole()
