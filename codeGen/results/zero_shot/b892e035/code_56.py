import sys

def calculate_probability():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        p = 1.0
        for i in range(n):
            P_A, A, B = map(int, sys.stdin.readline().split())
            p *= (P_A / 100) ** (A == B)
        print("{:.6f}".format(p))

calculate_probability()
