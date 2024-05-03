import sys

def calculate_probability():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        probabilities = []
        for _ in range(n):
            A, B, P = map(float, sys.stdin.readline().split())
            probabilities.append((A * P) + ((1 - P) * (1 - 0.5 ** n)))
        print(sum(probabilities))

if __name__ == "__main__":
    calculate_probability()
