import math

def calculate_probability():
    T = int(input())  # Read the number of test cases
    for _ in range(T):
        n = int(input())  # Read the number of tickets
        probs = []
        for _ in range(n):
            prob, a, b = map(float, input().split())  # Read the probability and numbers
            probs.append((prob * (1 - prob), a, b))  # Store the probability and numbers

        correct_orderings = math.factorial(n)  # Calculate the number of possible orderings
        for prob in probs:
            correct_orderings *= prob[0]  # Multiply the probabilities for each ordering

        threshold = 10**-6  # Threshold value for rounding errors
        if abs(correct_orderings - round(correct_orderings)) < threshold:
            print(0)  # Print 0 if the result is a rounding error
        else:
            print(round(correct_orderings))  # Print the rounded result

calculate_probability()
