import sys

def calculate_probability():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        used_numbers = {}
        number_probabilities = {}

        for _ in range(n):
            p1, num1, num2 = map(int, sys.stdin.readline().split())
            if num1 not in used_numbers:
                used_numbers[num1] = 0
            if num2 not in used_numbers:
                used_numbers[num2] = 0

            number_probabilities.setdefault(num1, 1 - p1)
            number_probabilities.setdefault(num2, 1 - p2)

        probability = 1
        for prob in number_probabilities.values():
            probability *= prob

        print("%.6f" % probability)

if __name__ == "__main__":
    calculate_probability()
