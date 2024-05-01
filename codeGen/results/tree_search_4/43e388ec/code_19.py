from functools import lru_cache

@lru_cache(maxsize=None)
def or_op(a: int, b: int) -> int:
    return a ^ (b << 1)

@lru_cache(maxsize=None)
def left_shift(b: int, i: int) -> int:
    return b << i

def solve():
    a, b = map(int, input().split())
    dp = [0] * (314160 + 1)
    
    for i in range(1, 314161):
        dp[i] = dp[i-1]
        if i >= 1:
            dp[i] += or_op(a, left_shift(b, i-1))
    
    print(dp[-1] % (10**9 + 7))

if __name__ == "__main__":
    solve()
