import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        and_res = 0
        xor_res = 0
        for _ in range(n):
            num = int(sys.stdin.readline())
            and_res &= num
            xor_res ^= num
        count = 1
        for i in range(30):
            if (and_res >> i) & 1:
                count *= (k - i)
            else:
                count *= i + 1
        print(count % (10**9 + 7))

if __name__ == "__main__":
    solve()
