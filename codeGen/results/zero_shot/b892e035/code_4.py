import sys

def calculate_probability():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        probabilities = []
        for _ in range(n):
            P, A, B = map(float, sys.stdin.readline().split())
            probabilities.append(P)
        probability = 1
        for P in probabilities:
            probability *= (1 / P)
        print("{:.6f}".format(probability))

calculate_probability()
