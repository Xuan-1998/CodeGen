import sys
from math import comb

T = int(input())  # Read number of test cases
for _ in range(T):
    n = int(input())  # Read number of tickets
    P1s = []  # Initialize list to store probabilities of first numbers
    B1s = []  # Initialize list to store first numbers
    for _ in range(n):
        P, A, B = map(int, input().split())  # Read probability and numbers for each ticket
        P1s.append(P)  # Store probability
        B1s.append(B)  # Store first number

    # Initialize the probability of correct numbering as 1 (since we can always get it right)
    total_prob = 1.0

    # Iterate over all possible combinations of numbers for each ticket
    for i in range(comb(n, n)):  # comb(n, n) is the number of ways to choose n items from a set of n items
        B2s = []  # Initialize list to store second numbers
        for _ in range(n):
            if (i >> _) % 2:  # If the i-th bit is 1, use the first number; otherwise, use the second number
                B2s.append(B1s[0])  # Use the first number
            else:
                B2s.append(B1s[1])  # Use the second number

        # Calculate the probability that the combination of numbers is correct
        prob = 1.0
        for j in range(n):
            if B2s[j] == 1:  # If the ticket has the first number, use its probability
                prob *= P1s[0]
            else:
                prob *= (1 - P1s[0])  # Otherwise, use the probability of the second number

        total_prob *= prob  # Multiply the probabilities for all combinations

    print(round(total_prob, 6))  # Print the final probability
