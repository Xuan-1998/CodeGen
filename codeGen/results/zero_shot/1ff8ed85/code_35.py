def can_send_over_network(t):
    cases = []
    for _ in range(t):
        n, *b = [int(x) for x in input().split()]
        b.sort()
        if min(b) == 1:
            print("YES")
        else:
            print("NO")

can_send_over_network(int(input()))
