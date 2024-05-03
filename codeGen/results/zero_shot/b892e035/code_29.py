import sys

def get_probabilities():
    t = int(sys.stdin.readline())
    probabilities = []
    
    for _ in range(t):
        n = int(sys.stdin.readline())
        probs = []
        
        for _ in range(n):
            p, a, b = map(int, sys.stdin.readline().split())
            probs.append((p, a, b))
        
        probabilities.append(probs)

    return probabilities

def calculate_probabilities(probabilities):
    total_prob = 1
    for probs in probabilities:
        numerator = 1
        denominator = 1
        
        for p, a, b in probs:
            numerator *= (p / 100)
            denominator *= (p / 100) + ((100 - p) / 100)
        
        total_prob *= numerator / denominator

    return total_prob

probabilities = get_probabilities()
total_prob = calculate_probabilities(probabilities)

print(f"{total_prob:.6f}")
