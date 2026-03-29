from functools import lru_cache

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    @lru_cache(None)
    def dp(i, left_hungry, right_hungry):
        if i == 0:
            return 0
        if left_hungry and right_hungry:
            return a[i] + max(dp(i-1, False, False), dp(i-1, True, True), dp(i-1, True, False))
        elif left_hungry and not right_hungry:
            return b[i] + max(dp(i-1, False, False), dp(i-1, True, False))
        elif not left_hungry and right_hungry:
            return c[i] + max(dp(i-1, False, True), dp(i-1, False, False))
        else:
            return 0

    print(max(dp(n-1, *[(True, False) if i > 0 else (False, False) for i in range(n)])))

if __name__ == "__main__":
    solve()
