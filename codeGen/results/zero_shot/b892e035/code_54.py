# Initialize variables
T = int(input())  # Number of test cases
probabilities = []

for _ in range(T):
    n = int(input())  # Number of tickets
    probability_matrix = []
    
    for _ in range(n):
        p1, num1, num2 = map(int, input().split())  # Probability and numbers for each ticket
        probability_matrix.append((p1, num1, num2))
    
    # Calculate the total probability of correct numbering
    total_probability = 1.0
    for (p1, _, _) in probability_matrix:
        total_probability *= p1
    
    probabilities.append(total_probability)

# Print the results
for p in probabilities:
    print(round(p, 6))  # Round to 6 decimal places
