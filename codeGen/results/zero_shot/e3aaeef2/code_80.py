def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        result = n
        for _ in range(m):
            new_result = 0
            while result > 0:
                digit = result % 10
                new_digit = (digit + 1) % 10 if digit < 9 else 0
                new_result = new_result * 10 + new_digit
                result //= 10
            result = new_result
        print(result % (10**9 + 7))

solve()
