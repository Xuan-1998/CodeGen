import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        count = 0
        for i in range(n):
            x = int(input()) & ((1 << k) - 1)
            if not (x & (x - 1)):
                count += 1
        print(count % (10**9 + 7))

if __name__ == "__main__":
    solve()
