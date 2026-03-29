code
u_counts = {}
l_counts = {}

for _ in range(int(input())):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    u_counts = {}
    l_counts = {}

    for r in U:
        if r not in u_counts:
            u_counts[r] = 0
        u_counts[r] += 1

    for r in L:
        if r not in l_counts:
            l_counts[r] = 0
        l_counts[r] += 1

    sequences = [0] * (C + 1)

    for i in range(1, C + 1):
        sequences[i] = (sequences[i - 1] + u_counts.get(i, 0) * l_counts.get(i, 0)) % (10**9 + 7)

    print(*sequences[1:], sep=' ')
