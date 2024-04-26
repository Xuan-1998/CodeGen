def will_enter_hole(N, x, k):
    # Calculate the ball's final position after bouncing
    total_distance = k * ((N // k) + 1)
    
    # Check if the ball's final position is equal to x
    if total_distance == x:
        return "YES"
    else:
        return "NO"


T = int(input())
for _ in range(T):
    N, x, k = map(int, input().split())
    print(will_enter_hole(N, x, k))
