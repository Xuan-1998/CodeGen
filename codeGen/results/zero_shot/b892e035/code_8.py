T = int(input())  
probabilities = []
for _ in range(T):
    n = int(input())  
    probs = [list(map(int, input().split())) for _ in range(n)]  
    probabilities.append(probs)

def calculate_probability(probabilities):
    total_prob = 1.0
    for prob in probabilities:
        num_prob, _, _ = prob
        total_prob *= (num_prob / 100)  
    return total_prob

for probs in probabilities:
    print(calculate_probability(probs))
