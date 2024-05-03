n = int(input())
probabilities = []
for _ in range(n):
    probs = list(map(int, input().split()))
    probabilities.append((probs[0], probs[1], probs[2]))

for probs in probabilities:
    print(calculate_probability(probs))

def calculate_probability(probs):
    n = len(probs)
    total_prob = 1
    for i in range(n):
        prob = probs[i][0] / (n - i) * probs[i][2] / (n - i)
        total_prob *= prob
    return round(total_prob, 6)
