import sys
import math

def main():
    T = int(input())  # number of test cases
    for _ in range(T):
        n = int(input())  # number of tickets
        probs = []
        for _ in range(n):
            p1, num1, num2 = map(float, input().split())
            probs.append(p1)
        correct_prob = 1.0
        for i in range(16):  # iterate over all possible numbers
            if len([prob for prob, num in zip(probs, [num1, num2]) if math.isclose(prob, i/16)]) == n:
                correct_prob *= i/16  # multiply by the probability of this number
        print(round(correct_prob, 6))  # round to 10^-6 precision

if __name__ == "__main__":
    main()
