def solve(n, m):
    res = len(str(n))  # initial length
    for _ in range(m):
        new_n = int(''.join(str(int(d) + 1) for d in str(n)))
        if new_n >= 10**9 + 7:  # if new_n is too large, increase the length
            res += 1
        else:
            res = len(str(new_n))  # update the length normally
    return res % (10**9 + 7)
