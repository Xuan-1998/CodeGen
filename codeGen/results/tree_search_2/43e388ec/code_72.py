def solve():
    a, b = map(int, input().split())
    mod = 10**9 + 7

    # Initialize the dictionary
    d = {(0, 0): 0}

    for i in range(1, 314160):
        for a_val in range(b):
            if (a_val, 0) not in d:
                d[(a_val, 0)] = 0
            if (a_val, i-1) in d:
                left_shifted_b = b << 1 if (b >> (i - 1)) & 1 else b
                d[(a_val, i)] = (d.get((a_val, i-1), 0) + a_val ^ left_shifted_b) % mod

    # Calculate the final result
    ans = 0
    for a_val in range(a):
        if (a_val, 314159) not in d:
            continue
        ans = (ans + d[(a_val, 314159)]) % mod

    print(ans)
