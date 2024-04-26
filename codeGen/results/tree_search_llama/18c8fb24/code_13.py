def hall_ball(N, x, k):
    if x <= 0 or x >= N+1:
        return "NO"
    
    if x == 0 or x == N+1:
        return "YES"

    remainder = (x % (k*2))
    if remainder == 0:
        return "YES"
    else:
        return "NO"


T = int(input())
for _ in range(T):
    N, x, k = map(int, input().split())
