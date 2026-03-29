def length_after_operations(n, m):
    if m == 0:
        return len(str(n)) % (10**9 + 7)

    new_n = n
    for _ in range(m):
        new_n = int(''.join(str(int(d) + 1) for d in str(new_n)))

    return len(str(new_n)) % (10**9 + 7)
