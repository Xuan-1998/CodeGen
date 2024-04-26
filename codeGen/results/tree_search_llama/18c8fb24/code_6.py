T = int(input())
for _ in range(T):
    N, x, k = map(int, input().split())
    print(will_ball_enter_hole(N, x, k))
