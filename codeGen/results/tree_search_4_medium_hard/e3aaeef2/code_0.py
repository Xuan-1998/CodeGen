dp = {(i, 0): i for i in range(1, 10**9 + 7)}
def solve(n, m):
    if (n, m) not in dp:
        last_digit = n % 10
        if last_digit == 9:
            new_digit = 0
        else:
            new_digit = last_digit + 1
        dp[(n, m)] = 1 + solve(n // 10, m - 1)
    return dp[(n, m)]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m) % (10**9 + 7))
