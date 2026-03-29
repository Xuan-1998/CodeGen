import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    if n <= k:
        print(s[:k])
    else:
        if k == 1:
            return print(min([s[i], s[-1]]))
        res1 = s[:-1]
        while len(res1) > k:
            res1 = res1[:-1]
        res2 = s + s[:k - n]
        print(min([res1, res2]))

if __name__ == "__main__":
    solve()
