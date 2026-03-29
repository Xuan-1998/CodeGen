def solve(t):
    MOD = 10**9 + 7
    for _ in range(t):
        n, m = map(int, input().split())
        length = len(str(n))
        for _ in range(m):
            new_n = int(''.join(str(d+1) for d in str(n)))
            n = new_n
            length = len(str(n))
        print(length % MOD)

t = int(input())
solve(t)
