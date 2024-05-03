import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    prob_total = 1.0
    for i in range(n):
        A, B, P = map(float, sys.stdin.readline().split())
        prob_total *= (P / 100) ** (A + B)
    print(prob_total)
