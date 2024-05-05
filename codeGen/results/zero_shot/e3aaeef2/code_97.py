def next_number(n):
    result = 0
    while n > 0:
        digit = n % 10
        result = (result * 10) + (digit + 1)
        n //= 10
    return result

def solve(n, m):
    for _ in range(m):
        n = next_number(n)
    return len(str(n)) % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
