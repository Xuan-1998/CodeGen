def solve(t):
    mod = 10**9 + 7
    for _ in range(t):
        n, m = map(int, input().split())
        result = str(n)
        for _ in range(m):
            new_result = ''
            for d in result:
                new_d = str(int(d) + 1)
                new_result += new_d
            result = new_result
        print(len(result) % mod)

t = int(input())
solve(t)
