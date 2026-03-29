from functools import lru_cache

def min_string(n, k):
    @lru_cache(None)
    def dp(i, j):
        if i == 0:
            return ("" if j == 0 else s[:j]) * ((1 << 30) if j > 0 else 1), False

        d = dp(i - 1, j)[1]
        if not d and i > 0:  # duplicate last character
            s2 = s[i - 1] + s[:i - 1]
            return dp(i - 1, j - 1)[0], True
        else:
            return (s[:i - 1] if not d else s[:i]) * ((1 << 30) if j > i else 1), d

    s = input().strip()
    res = dp(n, k)
    return min(res[0].rstrip(), s[:k].ljust(k)[::-1], key=lambda x: (x, len(x)))

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(min_string(n, k))
