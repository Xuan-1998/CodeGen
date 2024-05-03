import sys

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        P = [0] * (n + 1)
        P[0] = 1
        for i in range(1, n + 1):
            A, B, p = map(int, input().split())
            P[i] = (P[i - 1] * ((p / 100) if A != B else (2 * p / 100))) % (10 ** 9 + 7)
        print(P[-1])

if __name__ == "__main__":
    solve()
