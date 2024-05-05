import sys

def solve():
    MOD = 10**9 + 7
    dp = {0: 1}

    for _ in range(int(input())):
        n, k = map(int, input().split())
        ans = 0
        curr_xor = 0

        for _ in range(n):
            x = int(input())
            curr_xor ^= x
            ans += dp.get(curr_xor & ((1 << k) - 1), 0)
            ans %= MOD

        print(ans)

if __name__ == "__main__":
    solve()
