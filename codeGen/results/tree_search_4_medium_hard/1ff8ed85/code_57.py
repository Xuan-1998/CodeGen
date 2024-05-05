def can_send_over_network():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        a_parities = [0] * (n // 2 + 1)
        for i in range(n):
            if i % 2 == 0:
                a_parities[i // 2] += 1
            else:
                a_parities[i // 2] -= 1
        for i, p in enumerate(a_parities):
            if (i + 1) * (p % 2 == b[i]) % 2 == 0:
                print("YES")
                return
        print("NO")

can_send_over_network()
