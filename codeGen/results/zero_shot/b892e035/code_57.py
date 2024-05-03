import sys
from math import prod

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        probabilities = []
        for _ in range(n):
            A, B, P = map(float, sys.stdin.readline().split())
            probabilities.append((P, A, B))
        
        # Calculate the probability recursively
        correct_numbering = 1.0
        for P, A, B in probabilities:
            correct_numbering *= (1 - P) ** (n-1)
        
        print(correct_numbering)

if __name__ == "__main__":
    solve()
