import math

n = int(input())

for _ in range(n):
    n_tickets = int(input())
    probabilities = []

    for i in range(n_tickets):
        prob, a, b = map(float, input().split())
        probabilities.append((prob, a, b))

    for probs in probabilities:
        prob = 1.0
        used_numbers = set()

        for p, a, b in probs:
            if a not in used_numbers and b not in used_numbers:
                prob *= p
            elif a not in used_numbers:
                prob *= (1 - (1 - p) ** 0.5)
            else:
                prob *= (1 - (1 - p) ** 0.5)

        print(format(prob, ".6f"))
