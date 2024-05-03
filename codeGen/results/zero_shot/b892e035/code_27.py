import sys

def calculate_probability():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        p_a, a, b = map(float, sys.stdin.readline().split())
        p_b = 1 - p_a

        probability = 1
        for i in range(n):
            if i == 0:
                probability *= p_a
            else:
                probability *= (p_a * (1 - p_a) + p_b * (1 - p_b)) ** (n - i - 1)

        print(format(probability, ".6f"))

calculate_probability()
