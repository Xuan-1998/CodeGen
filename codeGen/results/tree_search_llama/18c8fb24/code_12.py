def will_ball_enter(x, N, k):
    # Calculate the distance from the initial position to the hole
    distance = abs(x - N // 2)
    
    # Check if this distance is a multiple of k
    return distance % k == 0

T = int(input())
for _ in range(T):
    N, x, k = map(int, input().split())
    print("YES" if will_ball_enter(x, N, k) else "NO")
