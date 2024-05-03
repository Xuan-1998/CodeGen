import sys
from math import comb, prod

def calculate_probability():
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        n = int(sys.stdin.readline())
        
        probabilities = [0.0]
        numbers = []
        
        for _ in range(n):
            p1, num1, num2 = map(float, sys.stdin.readline().split())
            
            probabilities.append(p1)
            numbers.append((num1, num2))
        
        total_probability = 0
        
        for i in range(1 << n):
            correct_count = 0
            
            for j in range(n):
                if (i & (1 << j)) != 0:
                    correct_count += 1
                    continue
            
            probability = prod(probabilities[j] ** (2 ** (correct_count - 1)) for j in range(n) if i & (1 << j))
            
            total_probability += probability
        
        print(total_probability)

calculate_probability()
