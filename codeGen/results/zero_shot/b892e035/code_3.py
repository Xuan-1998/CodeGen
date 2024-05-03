import math

def calculate_probability(n):
    total_probability = 1.0
    for _ in range(n):
        probability_not_A = 1 - float(_ + 1) / (2 ** (_ + 1))
        probability_not_B = 1 - float(_ + 1) / (2 ** (_ + 1))
        total_probability *= probability_not_A * probability_not_B
    return total_probability

T = int(input())  # Read the number of test cases
for _ in range(T):
    n = int(input())  # Read the number of tickets for each test case
    probabilities = []
    for _ in range(n):
        P, A, B = map(float, input().split())  # Read the probability and numbers for each ticket
        probabilities.append((P, A, B))
    total_probability = calculate_probability(n)
    print(total_probability)  # Print the result for each test case
