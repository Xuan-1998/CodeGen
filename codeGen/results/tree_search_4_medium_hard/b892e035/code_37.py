import sys
from collections import defaultdict

def calculate_probability():
    T = int(input())
    probabilities = []
    
    for _ in range(T):
        n = int(input())
        dp = defaultdict(float)
        dp[0] = 1.0
        
        for i in range(n):
            p, a, b = map(float, input().split())
            
            if a == b:
                probability = 0
            else:
                if p > 0.5:
                    probability = p * (1 - 2*p)
                else:
                    probability = p * 2 * (1-p)
            
            for j in range(i+1, n):
                dp[j] += dp[i] * probability
        
        probabilities.append(dp[n-1])
    
    for probability in probabilities:
        print(round(probability, 6))

calculate_probability()
