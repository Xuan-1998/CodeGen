from functools import lru_cache

def solve():
    a, b = map(int, input().split())
    @lru_cache(None)
    def dp(i, j):
        if i >= len(str(a)):
            return 0
        bit_a = int((a >> i) & 1)
        bit_b = (b >> j) & 1
        return ((bit_a ^ bit_b) % (10**9 + 7)) + dp(i+1, (j+1)%b)

    print(dp(0, 0))

if __name__ == "__main__":
    solve()
