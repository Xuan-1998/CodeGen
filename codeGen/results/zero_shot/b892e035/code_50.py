import sys

def calculate_probability():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        probabilities = []
        numbers = []
        for _ in range(n):
            prob1, num1, num2 = map(float, sys.stdin.readline().split())
            probabilities.append(prob1)
            numbers.append((num1, num2))
        
        probability = 1
        prev_num = None
        for i, (prob1, num) in enumerate(numbers):
            if i > 0 and num[0] == prev_num:
                probability *= (1 - prob1)
            else:
                probability *= prob1
            prev_num = num[0]
        
        print(round(probability, 6))

calculate_probability()
