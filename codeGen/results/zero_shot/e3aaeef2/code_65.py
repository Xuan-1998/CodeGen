import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        result_len = len(str(n))
        for _ in range(m):
            new_n = 0
            dig_len = len(str(n))
            for i in range(dig_len):
                digit = int((str(n))[i])
                new_digit = (digit + 1) % 10
                new_n = new_n * 10 + new_digit
            n = new_n
        print(len(str(n)) % (10**9 + 7))

solve()
