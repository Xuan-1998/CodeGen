def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        while m > 0:
            last_digit = (n % 10) + 1
            if last_digit == 10:
                last_digit = 1
            n //= 10
            n += last_digit * (10 ** (m % len(str(n))))
            m -= len(str(n)) - 1
        print(len(str(n)) % (10**9+7))

if __name__ == "__main__":
    solve()
