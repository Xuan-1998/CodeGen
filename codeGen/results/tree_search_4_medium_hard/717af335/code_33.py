def min_xor(A, B):
    dp = {}

    for x in range(min(A, B) + 1):
        a_x = A - x
        b_xor = B ^ x

        if a_x == x + (b_xor - x):
            dp[(A, B)] = x

    return dp.get((A, B), -1)

A = int(input())
B = int(input())

print(min_xor(A, B))
