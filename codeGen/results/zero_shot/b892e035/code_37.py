import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    probs = []
    for i in range(n):
        P, A, B = map(int, sys.stdin.readline().split())
        probs.append(P)
    prob = calculate_probability(n, probs)
    print(prob)

def calculate_probability(n, probs):
    prob = 1
    for i in range(n):
        prob *= probs[i]
    return prob
