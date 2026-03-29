def solve(n, m):
    if n < 10:
        return len(str(n + m)) % (10**9 + 7)
    else:
        return len(str(n + m - 1)) % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
