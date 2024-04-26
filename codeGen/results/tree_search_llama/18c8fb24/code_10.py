def will_enter_hole(N, x, k):
    for i in range(1, N + 1):
        a_i = (x - i) % (2 * k)
        if a_i == 0:
            return "YES"
    return "NO"

T = int(input())
for _ in range(T):
    N, x, k = map(int, input().split())
    print(will_enter_hole(N, x, k))
