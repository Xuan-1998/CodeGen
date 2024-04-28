from sys import stdin

dp = {}

def left_shift(x):
    return x << 1

def xor(a, b):
    return a ^ b

def solve():
    a, b = map(int, stdin.readline().split())
    total_sum = 0
    for i in range(315160):  # include 314159 and 0
        if (a, i) not in dp:
            if a == 0:
                dp[(a, i)] = left_shift(b, i)
            else:
                dp[(a-1, i)] = xor(a-1, left_shift(b, i))
            total_sum += dp[(a, i)]
        else:
            total_sum += dp[(a, i)]
    print(total_sum % (10**9 + 7))

solve()
