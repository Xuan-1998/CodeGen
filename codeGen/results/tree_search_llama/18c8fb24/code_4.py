def will_enter_hole(T):
    for _ in range(T):
        N, x, k = map(int, input().split())
        if x % k == 0:
            print("YES")
        else:
            d = (k - (x % k)) // k
            if x == d * k:
                print("YES")
            else:
                print("NO")

T = int(input())
will_enter_hole(T)
