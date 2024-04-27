def will_enter_hole(N, x, k):
    if x % k == 0 or N+1 % k == 0:
        return "YES"
    d = (x + k - 1) % (N+2) - x
    if d == 0:
        return "YES"
    return "NO"

T = int(input())
for _ in range(T):
    N, x, k = map(int, input().split())
    print(will_enter_hole(N, x, k))
