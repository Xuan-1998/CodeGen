import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        and_count = [0] * (k + 1)
        xor_count = [0] * (k + 1)
        for _ in range(n):
            num = int(sys.stdin.readline())
            for i in range(k, -1, -1):
                bit = (num >> i) & 1
                and_count[i] += bit
                xor_count[i] += (bit ^ 1)
        count = 0
        for i in range(k + 1):
            if and_count[i] >= xor_count[i]:
                count += 2 ** i
        print(count % (10**9 + 7))

if __name__ == "__main__":
    solve()
