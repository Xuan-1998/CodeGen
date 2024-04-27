def will_ball_enter_hole():
    T = int(input())
    for _ in range(T):
        N, x, k = map(int, input().split())
        # Check if the ball will enter the hole on its forward journey
        if x % k == 0 or (N+1) % k == 0:
            print("YES")
        else:
            # Calculate the remainder when N+1 is divided by k
            remaining_tiles = (N+1) % k
            # Check if it's equal to x
            if remaining_tiles == x % k:
                print("YES")
            else:
                print("NO")

will_ball_enter_hole()
