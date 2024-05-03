import sys
from math import prod

T = int(sys.stdin.readline())
probabilities = []

for _ in range(T):
    n = int(sys.stdin.readline())
    state = set()
    probabilities.append(1)

    for _ in range(n):
        p1, num1, num2 = map(float, sys.stdin.readline().split())
        if num1 not in state:
            state.add(num1)
        if num2 not in state:
            state.add(num2)
        probabilities[-1] *= (p1 if num1 not in state else 0) * (1 - p1) + (p1 if num2 not in state else 0) * (1 - p1)

    print(round(prod(probabilities[-1]), 6))
