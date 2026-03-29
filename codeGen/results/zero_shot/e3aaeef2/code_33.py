def solve(t):
    mod = 10**9 + 7
    for _ in range(t):
        n, m = map(int, input().split())
        count = [0] * 10
        for _ in range(m):
            new_n = 0
            while n:
                d = n % 10
                if d < 9:  # replace digit
                    new_n = new_n * 10 + (d + 1)
                    count[d] += 1
                else:  # digit is 9, so it's replaced with 0
                    new_n = new_n * 10
                    count[0] += 1
                n //= 10
            n = new_n
        print(count.count(1) % mod)

if __name__ == '__main__':
    t = int(input())
    solve(t)
