n = int(input())
probabilities = []
for _ in range(n):
    P, A, B = map(float, input().split())
    P_total = P * (1 - P)
    probabilities.append(P_total)

cumulative_prob = 0
for prob in probabilities:
    cumulative_prob += prob

print(cumulative_prob)
