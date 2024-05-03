import math

def calculate_probability():
    T = int(input())  # Read the number of test cases
    for _ in range(T):
        n = int(input())  # Read the number of tickets
        probabilities = []
        for _ in range(n):
            P1, A1, B1 = map(float, input().split())
            P2, A2, B2 = map(float, input().split())
            probabilities.append((P1, A1, B1))
            probabilities.append((P2, A2, B2))

        correct_numbering_probability = 1
        for i in range(n):
            probability = (probabilities[i][0] * probabilities[(i+1)%n][0]) / (
                sum(probabilities[j][0] for j in range(n))
            )
            correct_numbering_probability *= probability

        print(math.floor(correct_numbering_probability + 0.00001))  # Round to 6 decimal places and floor

calculate_probability()
