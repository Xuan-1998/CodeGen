import sys
from collections import defaultdict

def calculate_probability():
    n = int(input())
    
    dp = defaultdict(lambda: 0)
    dp[(0, 0, 0)] = 1
    
    for _ in range(n):
        ticket_probabilities = [int(x) for x in input().split()]
        
        count1, count2, p1, p2 = 0, 0, ticket_probabilities[0], ticket_probabilities[1]
        
        for i in range(2):
            if ticket_probabilities[i] > count1:
                count1 += 1
            elif ticket_probabilities[i] < count2:
                count2 += 1
        
        dp[(n - _ - 1, count1, count2)] = (dp.get((n - _ - 1, count1 - 1, count2), 0) * p1 * (1 - p1/16)**(n - _ - 1) if count1 > 0 else 
                                              dp.get((n - _ - 1, count1, count2 - 1), 0) * (1 - p1/16) * p2 * (1 - p2/16)**(n - _ - 1) if count2 > 0 else 
                                              (dp[(n - _ - 1, 0, 0)] * p1 * (1 - p1/16)**(n - _ - 1) if count1 == 0 and count2 == 0 else 0))
    
    return dp[(0, 0, 0)]

print(calculate_probability())
