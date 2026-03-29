import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        ans = n
        for _ in range(m):
            ans = sum(int(d) + 1 for d in str(ans))
        print(len(str(ans)) % (10**9 + 7))

if __name__ == "__main__":
    solve()
