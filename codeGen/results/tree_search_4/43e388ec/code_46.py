import sys
from functools import reduce

def solve():
    a = int(input(), 2)
    b = int(input(), 2)

    dp = [0] * (314160)
    dp[0] = a ^ b

    for i in range(1, 314160):
        dp[i] = (a ^ ((b >> i) & 1)) % (10**9 + 7)

    print(reduce(lambda x, y: (x + y) % (10**9 + 7), dp))

if __name__ == "__main__":
    solve()
