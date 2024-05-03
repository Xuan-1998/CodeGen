n = int(input())
probabilities = []
for _ in range(n):
    p, a, b = map(int, input().split())
    probabilities.append((p, a, b))
ticket_probabilities = []
for prob, a, b in probabilities:
    p_a = (prob / 100) * (1 - (1 - (a / (16 ** 2))))
    p_b = 1 - p_a
    ticket_probabilities.append((p_a, p_b))
answer = 1
for prob_a, prob_b in ticket_probabilities:
    answer *= (prob_a * prob_b)
print(answer)
