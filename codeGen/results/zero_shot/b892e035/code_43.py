import sys

def get_probabilities():
    T = int(sys.stdin.readline())
    probabilities = []
    for _ in range(T):
        n = int(sys.stdin.readline())
        prob = 1.0
        for _ in range(n):
            P, A, B = map(float, sys.stdin.readline().split())
            prob *= (P * (A != B) + (1 - P) / 2)
        probabilities.append(prob)
    return probabilities

probabilities = get_probabilities()
for prob in probabilities:
    print('{:.6f}'.format(prob))
