import sys

def left_shift(b, i):
    return int(str(b) + '0' * i, 2)

def xor_sum(a, b):
    mod = 10**9 + 7
    dp = { (a, b): ((a ^ b) % mod) }
    for i in range(1, 315160):
        new_a = left_shift(b, i - 1)
        if (new_a, b) not in dp:
            dp[(new_a, b)] = xor_sum(new_a, a) % mod
        dp.setdefault((a, b), 0)
        a, b = new_a, b
    return sum(dp.values()) % mod

# Read input from standard input
a, b = map(int, input().split())
print(xor_sum(a, b))
