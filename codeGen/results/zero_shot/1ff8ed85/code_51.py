def can_send_over_network():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        a = [0]
        for i in range(1, n):
            a.append(a[i-1] + b[i])
        canSend = True
        for i in range(n):
            if b[i] > a[i]:
                canSend = False
                break
        print("YES" if canSend else "NO")

can_send_over_network()
