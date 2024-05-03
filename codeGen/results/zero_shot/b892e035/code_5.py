import sys
from math import prod

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        probs = []
        for _ in range(n):
            p1, a1, b1 = map(float, sys.stdin.readline().split())
            probs.append((p1, a1, b1))
        
        # Calculate the probability of correct numbering
        prob = prod(p1 * (a1 != b1) + p2 * (a1 == b2 and b1 == b2) for _, (p1, a1, b1), (_, p2, a2, b2) in zip(range(n), probs, probs))
        
        print(round(prob, 6))  # Round to 10^-6

if __name__ == "__main__":
    solve()
