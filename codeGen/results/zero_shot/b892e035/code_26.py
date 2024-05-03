import math
T = int(input())  # Read T test cases

for _ in range(T):
    n = int(input())  # Read number of tickets
    probs = []  # Initialize list for probabilities
    
    for _ in range(n):
        prob1, num1, num2 = map(float, input().split())  # Read probability and numbers for each ticket
        probs.append((prob1 * (1 - prob1), prob1))  # Calculate probability of correct numbering and store it along with the number
        
    total_prob = 0  # Initialize total probability
    
    for i in range(n):  # Loop through each ticket
        if i == 0:
            total_prob += probs[i][0]  # Add probability without considering other tickets
        else:
            total_prob *= (1 - probs[i-1][1]) * (1 - probs[i][1])  # Calculate probability considering previous tickets
    
    print(math.exp(total_prob))  # Print the final probability
