def calculate_probability():
    T = int(input())
    for _ in range(T):
        n = int(input())
        probabilities = []
        numbers = []
        for i in range(n):
            p, a, b = map(int, input().split())
            probabilities.append(p)
            numbers.append((a, b))
        
        # Calculate the probability of correct numbering
        total_probability = 1.0
        for i in range(len(numbers)):
            if i > 0:
                total_probability *= (probabilities[i-1] * (1 - probabilities[i-1])) / len(set([x[0] for x in numbers[:i]] + [y[1] for y in numbers[:i]]))
        
        print(format(total_probability, '.6f'))
