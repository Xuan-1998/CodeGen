import sys
from math import comb

def prob_calculator():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        probs = []
        numbers = []
        for _ in range(n):
            probs.append(float(sys.stdin.readline()))
            numbers.append([int(sys.stdin.readline()), int(sys.stdin.readline())])
        
        # Sort the probabilities and numbers
        sorted_probs = sorted(probs)
        sorted_numbers = [sorted(x) for x in zip(*numbers)]
        
        # Initialize the probability of correct numbering
        prob = 1
        
        # Calculate the probability using combinatorics
        for i, (p1, p2) in enumerate(zip(sorted_probs, sorted_numbers)):
            num_ways = comb(n - i - 1, i)
            prob *= p1 * p2 / ((1 - p1 + p2) ** (n - i - 1))
        
        # Print the result
        print(f"{prob:.6f}")

if __name__ == "__main__":
    prob_calculator()
