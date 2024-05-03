import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    probabilities = []
    for _ in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        probabilities.append((line[0], line[1], line[2]))
    
    correct_probabilities = []
    for p1, a, b in probabilities:
        correct_probability = p1 * (1 if a != b else 0)
        correct_probabilities.append(correct_probability)

    overall_probability = 1
    for p in correct_probabilities:
        overall_probability *= p

    print(overall_probability)
