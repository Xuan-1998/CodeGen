import sys

def main():
    T = int(sys.stdin.readline())  # Read number of test cases
    for _ in range(T):
        n = int(sys.stdin.readline())  # Read number of tickets
        P = []  # Initialize list to store probabilities
        for i in range(n):
            A, B = map(int, sys.stdin.readline().split())  # Read probability and numbers for this ticket
            P.append([A, B])
        
        total_probability = 1.0  # Initialize with 1.0
        for i in range(n):
            A_prob = P[i][0] / (P[i][0] + P[i][1])  # Probability of A_i
            B_prob = P[i][1] / (P[i][0] + P[i][1])  # Probability of B_i
            total_probability *= (A_prob * (1 - A_prob) + B_prob * (1 - B_prob))  # Calculate the probability for this ticket
        
        print(format(total_probability, ".6f"))  # Round to 6 decimal places and print

if __name__ == "__main__":
    main()
