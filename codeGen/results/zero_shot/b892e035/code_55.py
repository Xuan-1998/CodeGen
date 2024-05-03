import sys

def calculate_probability():
    n = int(input())  # Read n (the number of tickets)
    total_probability = 1  # Initialize total probability
    
    for _ in range(n):
        P_i, A_i, B_i = map(float, input().split())  # Read probabilities and numbers
        total_probability *= (1 - P_i) * (1 - B_i)  # Calculate the product
        
    print(total_probability)  # Print the calculated probability

if __name__ == "__main__":
    calculate_probability()
