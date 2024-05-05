    ops = 0
    while n > 9:
        ops += len(str(n))
        n = sum(int(d) + 1 for d in str(n))
    print(len(str(n)) % (10**9+7))
