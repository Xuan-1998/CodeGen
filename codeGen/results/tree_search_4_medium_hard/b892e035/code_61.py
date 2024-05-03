from functools import lru_cache

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        p1s, p2s = [], []
        for _ in range(n):
            p1, num1, num2 = map(float, input().split())
            p1s.append(p1)
            p2s.append((num1, num2))
        @lru_cache(None)
        def prob(i, correct):
            if i == n:
                return 1.0
            res = 0
            for j in range(2):
                for k in (0, 1):
                    if not correct or k != p2s[i][j]:
                        res += p1s[i] * prob(i + 1, correct and j == 0)
            return res
        print(prob(0, True))

if __name__ == "__main__":
    solve()
