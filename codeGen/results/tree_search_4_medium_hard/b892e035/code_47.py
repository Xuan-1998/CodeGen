import sys

def calculate_probability():
    T = int(input())  # read number of test cases
    for _ in range(T):
        n = int(input())  # read number of tickets
        probabilities = [0] * (n + 1)
        
        # base case: only one ticket
        if n == 1:
            probability = float(input().split()[2])  # read second number's probability
            probabilities[1] = probability
        
        else:
            for i in range(2, n + 1):
                probabilities[i] = 0.5 * (probabilities[i - 1] + ((1 - probabilities[i - 1]) / (2 ** (i - 1)))))
        
        print(probabilities[-1])  # output probability of correct numbering for the last ticket

calculate_probability()
