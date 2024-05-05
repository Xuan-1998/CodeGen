import sys

def solve():
    t = int(sys.stdin.readline().strip())
    memo = {}

    def dfs(n, m):
        if (n, m) in memo:
            return memo[(n, m)]
        
        if m == 0:
            return len(str(n))

        res = 0
        while n > 0:
            d = n % 10
            if d > 0:
                res += 1
            n //= 10

        new_n = (d + 1) * (10 ** res) + n
        memo[(n, m)] = len(str(new_n)) - res
        return memo[(n, m)]

    for _ in range(t):
        n, m = map(int, sys.stdin.readline().strip().split())
        print(dfs(n, m))

if __name__ == "__main__":
    solve()
