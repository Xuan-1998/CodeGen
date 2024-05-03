n = int(input())
probs = []

for _ in range(n):
    prob_a, a, b = map(float, input().split())
    probs.append((prob_a, a, b))

total_prob = 1.0

for prob_a, a, b in probs:
    if a == b:
        continue
    total_prob *= (prob_a * (1 - prob_a))

print(round(total_prob, 6))
