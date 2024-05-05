import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        result_len = len(str(n))
        while m > 0:
            new_n = str(n)
            for i in range(len(new_n)):
                digit = int(new_n[i])
                new_n = new_n[:i] + str(digit + 1) + new_n[i+1:]
            n = int(new_n)
            result_len += (len(str(n)) - len(str(int(n))))
            m -= 1
        print(result_len % (10**9 + 7))

if __name__ == "__main__":
    solve()
