import math
from collections import defaultdict

def calculate_probability():
    T = int(input())
    for _ in range(T):
        n = int(input())
        probabilities = []
        numbers = set()
        for _ in range(n):
            p1, num1, num2 = map(float, input().split())
            probabilities.append(p1)
            if num1 not in numbers:
                numbers.add(num1)
            if num2 not in numbers:
                numbers.add(num2)
        total_probability = 1
        for i, prob in enumerate(probabilities):
            total_probability *= (prob / sum(probabilities)) * (len(numbers) == i + 1)
        print('{:.6f}'.format(total_probability))

calculate_probability()
