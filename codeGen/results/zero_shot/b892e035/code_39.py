T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    A = []
    B = []
    P = []
    for i in range(n):
        p1, a, b = map(int, sys.stdin.readline().split())
        A.append(a)
        B.append(b)
        P.append(p1)
    prob = calculate_probability(n, A, B, P)
    print("%.6f" % prob)  # round to 6 decimal places
