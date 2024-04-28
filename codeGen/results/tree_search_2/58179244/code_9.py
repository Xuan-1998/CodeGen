from collections import defaultdict

def solve():
    n = int(input())
    s = input()

    dp = [[0] * 3 for _ in range(n + 1)]
    memo = defaultdict(dict)

    def dfs(i, c):
        if i == 0:
            return 1
        if (i, c) in memo:
            return memo[(i, c)]

        res = 0
        for j in range(3):
            if (j != c and s[i - 1] == chr(ord('R') + j)):
                res += dfs(i - 1, j)
        memo[(i, c)] = res
        return res

    res = dfs(n, 2)  # Initialize the result as the number of diverse garlands with the last lamp being 'B'
    for i in range(3):
        if s[0] == chr(ord('R') + i):
            res -= dfs(1, i)

    print(res)
    diverse_s = ""
    i, c = n, 2
    while i > 0:
        diverse_s = chr(ord('R') + (c % 3)) + diverse_s
        for j in range(3):
            if (j != c and s[i - 1] == chr(ord('R') + j)):
                dfs(i - 1, j)
                break
        c = (c + 1) % 3
        i -= 1

    print(diverse_s)

if __name__ == "__main__":
    solve()
